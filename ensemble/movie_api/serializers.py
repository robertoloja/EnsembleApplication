from rest_framework import serializers
from movie_api.models import Movie

class MovieSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = [
      'title',
      'description',
      'release_year',
      'duration',
      'rating',
      'likes',
    ]