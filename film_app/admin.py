from django.contrib import admin

from film_app.models import (
    Movie,
    Actor,
    Genre,
    Category,
)

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Category)
