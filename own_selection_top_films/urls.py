from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('film_app.routers')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]
