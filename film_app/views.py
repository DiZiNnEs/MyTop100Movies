from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from film_app.models import Film
from film_app.serializers import FilmSerializers, CreateFilmSerializer


class FilmViews(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateFilmView(APIView):
    def post(self, request):
        review = CreateFilmSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)
