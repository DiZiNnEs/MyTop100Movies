from django.contrib.auth.models import User
from django.db import models


class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} + {self.title}'
