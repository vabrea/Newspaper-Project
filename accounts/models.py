from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

class Language(models.Model):
    key = models.CharField(max_length=4)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        blank = True,
        null= True)
    preferred_language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

