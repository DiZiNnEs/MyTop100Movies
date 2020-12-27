from rest_framework import serializers

from film_app.models import Film


class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['title', 'description', 'publication_date']
