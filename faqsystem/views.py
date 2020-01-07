from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from django.db.models.functions import Greatest
from functools import partial
from .models import FAQ, Images

import multiprocessing as mp

# Create your views here.
def score(query, target):
    table = [i for i in range(len(query) + 1)]
    score = 0
    tolerance = len(query) // 3 + 1
    ubound = min(len(table), tolerance + 2)
    for j in range(len(target)):
        for i in range(1, ubound):
            prev = table[i]
            table[i] = min(table[0] + (query[i - 1] != target[j]), min(table[i] + 1, table[i - 1] + 1))
            table[0] = prev
        table[0] = 0
        while True:
            ubound -= 1
            if table[ubound] <= tolerance:
                break
        ubound = min(len(table), ubound + 2)
        score = score + ((tolerance - table[-1] + 1) / (table[-1] + 1) if table[-1] <= tolerance else 0)
    return score

class FAQView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'faq_list'

    def get_queryset(self):
        """Return the last five published questions."""
        query = self.request.GET.get('query')
        if query is not None and query is not '':
            listed = list(FAQ.objects.all())
            scores = [0 for _ in range(len(listed))]
            for q in query.split():
                query_score = partial(score, q)
                with mp.Pool() as p:
                    scores = [x + y for x, y in zip(scores, p.map(query_score, [str(x) for x in listed]))]
            filtered = [x for s, x in sorted(zip(scores, listed), key=lambda entry: entry[0], reverse=True) if s > 0]
            return filtered

            # return FAQ.objects.annotate(search=SearchVector('question_text', 'answer_text')).annotate(similarity=Greatest(
            #     TrigramSimilarity('question_text', query),
            #     TrigramSimilarity('answer_text', query)
            # )).filter(similarity__gte=0.1).order_by('-similarity')

        return FAQ.objects.all()
