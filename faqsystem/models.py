from django.db import models

import os

# Create your models here.
class FAQ(models.Model):
    question_text = models.CharField(max_length=10000)
    answer_text = models.CharField(max_length=10000)

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
