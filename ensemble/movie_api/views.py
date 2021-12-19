from .models import Movie
from .serializers import MovieSerializer
from rest_framework import filters, permissions, generics
from rest_framework.decorators import api_view
from django.http import JsonResponse

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


@api_view(['PATCH'])
def like_movie(request, pk):
  movie = Movie.objects.filter(pk=pk).first()
  movie.likes = movie.likes + 1
  movie.save()
  return JsonResponse({1: movie.likes})

@api_view(['PATCH'])
def dislike_movie(request, pk):
  movie = Movie.objects.filter(pk=pk).first()
  movie.likes = movie.likes - 1
  movie.save()
  return JsonResponse({1: movie.likes})