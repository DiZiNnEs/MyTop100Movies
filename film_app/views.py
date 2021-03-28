from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from film_app.models import Movie
from film_app.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        user = self.request.user
        return Movie.objects.filter(user=user)
