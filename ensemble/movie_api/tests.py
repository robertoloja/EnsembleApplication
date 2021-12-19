from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient, force_authenticate, APIRequestFactory
from rest_framework.parsers import JSONParser
from .models import Movie
from .views import MovieList
from datetime import date, timedelta
import io


class APITests(TestCase):
  def setUp(self):
    release_date = date.fromisoformat('2019-01-01')
    length = timedelta(minutes=20, hours=1)

    Movie(title="A movie", 
          description="foo",
          release_year=release_date,
          duration=length).save()

    Movie(title="doesn't come up in search", 
          description="foo",
          release_year=release_date,
          duration=length).save()
    
    User(username="test", password="pass").save()
  
  def get_json_response(self, endpoint):
    client = APIClient()
    response = client.get(endpoint)
    content = io.BytesIO(response.content)
    return JSONParser().parse(content)


  def test_api_get(self):
    all_movies = self.get_json_response('/movies/')
    self.assertEqual(len(all_movies), 2)
  

  def test_api_post(self):
    new_movie = {
      "title": "new",
      "description": "baz",
      "duration": "00:35:00",
      "release_year": "2020-02-02",
    }
    response = APIClient().post('/movies/', new_movie, format='json')

    # unauthenticated POST request fails
    self.assertEqual(response.status_code, 403)

    user = User.objects.first()
    view = MovieList.as_view()
    request = APIRequestFactory().post('/movies/', new_movie, format='json')
    force_authenticate(request, user)
    response = view(request)

    # authenticated users can make POST requests
    self.assertEqual(response.status_code, 201)

  
  def test_search(self):
    search_results = self.get_json_response('/movies/?search=movie')
    self.assertEqual(len(search_results), 1)
  

  def test_like_movie(self):
    movie = Movie.objects.first()
    original_number_of_likes = movie.likes
    APIClient().patch('/movies/' + str(movie.id) + '/like/')
    self.assertEqual(original_number_of_likes + 1, Movie.objects.first().likes)

  def test_dislike_movie(self):
    movie = Movie.objects.first()
    original_number_of_likes = movie.likes
    APIClient().patch('/movies/' + str(movie.id) + '/dislike/')
    self.assertEqual(original_number_of_likes - 1, Movie.objects.first().likes)