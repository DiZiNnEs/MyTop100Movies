from rest_framework import generics
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from film_app.models import Movie
from film_app.serializers import MovieSerializer


class FilmViews(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class FilmDetailView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        q = Movie.objects.filter(user=self.request.user)
        return q


class CreateFilmView(generics.CreateAPIView):
    queryset = Movie
    serializer_class = MovieSerializer
