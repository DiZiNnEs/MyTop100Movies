from django.urls import path

from film_app.views import FilmViews, CreateFilmView

urlpatterns = [
    path('films/', FilmViews.as_view()),
    path('create-film/', CreateFilmView.as_view()),
]
