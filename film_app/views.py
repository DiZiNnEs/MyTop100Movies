from rest_framework import viewsets

from film_app.serializers import (
    MovieSerializer,
    CategorySerializer,
    ActorSerializer,
    GenreSerializer
)

from film_app.models import (
    Movie,
    Category,
    Genre,
    Actor
)


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        user = self.request.user
        return Movie.objects.filter(user=user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
