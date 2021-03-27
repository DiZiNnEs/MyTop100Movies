from rest_framework import viewsets

from film_app.models import Movie
from film_app.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
