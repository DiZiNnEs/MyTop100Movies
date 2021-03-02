from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from rest_framework.authtoken.models import Token

from datetime import date


class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    description = models.TextField('description')
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} + {self.title}'

    class Meta:
        db_table = 'film'
        verbose_name = 'Film'
        verbose_name_plural = 'Films'


class Category(models.Model):
    name = models.CharField('name', max_length=100)
    description = models.TextField('description')
    url = models.SlugField('url', max_length=160, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Genre(models.Model):
    name = models.CharField('name', max_length=100)
    description = models.TextField('description')
    url = models.SlugField('url', max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'genre'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Actor(models.Model):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    age = models.PositiveSmallIntegerField("age", default=0)
    photo = models.ImageField("photo of the actor")

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self) -> reverse:
        return reverse('actor detail', kwargs={'slug': self.first_name + ' ' + self.last_name})

    class Meta:
        db_table = 'actor'
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'


class Movie(models.Model):
    title = models.CharField('title', max_length=100)
    tagline = models.CharField('tagline', max_length=100, default='')
    description = models.TextField("description")
    poster = models.ImageField("poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("release data", default=2021)
    country = models.CharField("country", max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name='director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='actor', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='genre', related_name='film_genre')
    world_premiere = models.DateField("World premiere", default=date.today)
    budget = models.PositiveIntegerField("Budget", default=0, help_text='indicate dollar amounts')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
