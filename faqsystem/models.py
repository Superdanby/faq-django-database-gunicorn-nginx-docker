from django.db import models
from django.conf import settings
from django.utils.timezone import now

import os

# Create your models here.
class NonStrippingTextField(models.TextField):
    """A TextField that does not strip whitespace at the beginning/end of
    it's value.  Might be important for markup/code."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingTextField, self).formfield(**kwargs)

class FAQ(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    question_text = models.CharField(max_length=10000)
    answer_text = NonStrippingTextField(blank=True)
    clicks = models.BigIntegerField(default=0)

    def __str__(self):
        return self.question_text + self.answer_text


class Images(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.img.url


class Files(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    f = models.FileField(upload_to='files')

    def __str__(self):
        return self.f.url

    def filename(self):
        return os.path.basename(self.f.name)


class Feedback(models.Model):
    author = models.CharField(max_length=100)
    feedback = NonStrippingTextField()
    feedback_date = models.DateTimeField(default=now, editable=False)
    reply = NonStrippingTextField(blank=True)
    reply_date = models.DateTimeField(null=True, editable=False)

    def __str__(self):
        return self.feedback
