from rest_framework import serializers

from film_app.models import Film


class FilmSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Film
        fields = ['title', 'description', 'publication_date', 'user']
