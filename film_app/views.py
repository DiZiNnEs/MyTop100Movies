
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from film_app.models import Movie
from film_app.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'])
    def movie(self, request):
        q = self.queryset.filter(user=request.user)
        result = MovieSerializer(q).data
        return Response(result, status=status.HTTP_200_OK)
