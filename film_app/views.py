from rest_framework import generics
from rest_framework import mixins

from film_app.models import Film
from film_app.serializers import FilmSerializers


class FilmViews(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
