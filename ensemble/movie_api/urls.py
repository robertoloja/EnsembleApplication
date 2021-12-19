from django.urls import path
from . import views


urlpatterns = [
  path('movies/', views.MovieList.as_view()),
  path('movies/<int:pk>', views.MovieDetail.as_view())
]