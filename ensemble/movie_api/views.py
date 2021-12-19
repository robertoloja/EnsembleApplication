from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics

class MovieList(generics.ListCreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer