# Generated by Django 3.1.4 on 2021-03-02 13:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='age')),
                ('photo', models.ImageField(upload_to='', verbose_name='photo of the actor')),
            ],
            options={
                'verbose_name': 'Actors and directors',
                'verbose_name_plural': 'Actors and directors',
                'db_table': 'actor',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='tagline')),
                ('description', models.TextField(verbose_name='description')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='poster')),
                ('year', models.PositiveSmallIntegerField(default=2021, verbose_name='release data')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='World premiere')),
                ('budget', models.PositiveIntegerField(default=0, help_text='indicate dollar amounts', verbose_name='Budget')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='film_app.Actor', verbose_name='actor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='film_app.category', verbose_name='Category')),
                ('directors', models.ManyToManyField(related_name='film_director', to='film_app.Actor', verbose_name='director')),
                ('genres', models.ManyToManyField(related_name='film_genre', to='film_app.Genre', verbose_name='genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='description')),
                ('publication_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
                'db_table': 'film',
            },
        ),
    ]
