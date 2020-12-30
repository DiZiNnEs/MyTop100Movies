from django.urls import path

from film_app.views import FilmViews, CreateFilmView, CustomAuthToken

urlpatterns = [
    path('films/', FilmViews.as_view()),
    path('create-film/', CreateFilmView.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view())
]
