from rest_framework import serializers

from film_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
