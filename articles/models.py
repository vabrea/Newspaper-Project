from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Section(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()


    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])