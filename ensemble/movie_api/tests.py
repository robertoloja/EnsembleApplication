from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.parsers import JSONParser
from .models import Movie
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
  
  def get_json_response(self, endpoint):
    client = APIClient()
    response = client.get(endpoint)
    content = io.BytesIO(response.content)
    return JSONParser().parse(content)

  def test_api(self):
    self.assertEqual(0, 0)
  
  def test_search(self):
    print(self.get_json_response('/movies/?search=movie'))
    self.assertEqual(0, 0)