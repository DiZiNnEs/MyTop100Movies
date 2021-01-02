from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from rest_framework.authtoken.models import Token


class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} + {self.title}'


class Actor(models.Model):
    """Actors and directors"""
    first_name = models.CharField('First name', max_length=32)
    last_name = models.CharField('Last name', max_length=32)
    age = models.PositiveSmallIntegerField("Age", default=0)
    photo = models.ImageField("Photo of the actor")

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self) -> reverse:
        return reverse('actor detail', kwargs={'slug': self.first_name + ' ' + self.last_name})

    class Meta:
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'
