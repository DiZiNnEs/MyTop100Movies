from django.urls import path, include
from rest_framework.routers import DefaultRouter

from film_app.views import MovieViewSet


router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='Movies')

urlpatterns = [
    path('', include(router.urls)),
]
