# Generated by Django 3.1.4 on 2021-03-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0002_delete_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(upload_to='media/actors/photos/', verbose_name='photo of the actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='media/movies/posters/', verbose_name='poster'),
        ),
    ]
