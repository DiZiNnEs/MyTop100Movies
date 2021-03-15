from rest_framework import generics
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from film_app.models import Film
from film_app.serializers import FilmSerializers, CreateFilmSerializer


class FilmViews(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers


class FilmDetailView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

    def get_queryset(self):
        q = Film.objects.filter(user=self.request.user)
        return q


class CreateFilmView(generics.CreateAPIView):
    queryset = Film
    serializer_class = CreateFilmSerializer
