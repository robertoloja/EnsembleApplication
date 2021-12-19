from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics
from rest_framework import filters, permissions

class MovieList(generics.ListCreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['title']
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]