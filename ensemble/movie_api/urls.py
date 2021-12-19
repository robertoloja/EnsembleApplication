from django.urls import path
from . import views


urlpatterns = [
  path('movies/', views.MovieList.as_view()),
  path('movies/<int:pk>', views.MovieDetail.as_view()),
  path('movies/<int:pk>/like/', views.like_movie),
  path('movies/<int:pk>/dislike/', views.dislike_movie),
]