from django.urls import path

from film_app.views import FilmViews

urlpatterns = [
    path('films/', FilmViews.as_view()),
]
