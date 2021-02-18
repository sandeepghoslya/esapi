from rest_framework import serializers
from .models import MoviesDetails


class MoviesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
     model = MoviesDetails
     fields = ['id', 'title', 'released_year', 'rating', 'genres']