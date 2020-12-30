from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


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


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
