from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


from film_app.models import Film
from film_app.serializers import FilmSerializers, CreateFilmSerializer


class FilmViews(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers


class CreateFilmView(CreateAPIView):
    queryset = Film
    serializer_class = CreateFilmSerializer
