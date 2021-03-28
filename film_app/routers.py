from django.urls import path, include
from rest_framework.routers import DefaultRouter

from film_app.views import MovieViewSet


router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='Movies')
router.register(r'categories', MovieViewSet, basename='Categories')
router.register(r'movies', MovieViewSet, basename='Movies')
router.register(r'movies', MovieViewSet, basename='Movies')

urlpatterns = [
    path('', include(router.urls)),
]
