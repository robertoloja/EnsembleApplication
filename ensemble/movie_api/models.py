from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
  title = models.CharField(max_length=100, blank=False, default='')
  description = models.CharField(max_length=500, blank=False, default='')
  release_year = models.DateField(auto_now=False, blank=False)
  duration = models.DurationField(blank=False)
  rating = models.IntegerField(
    default = 1,
    validators = [MaxValueValidator(5), MinValueValidator(1)]
  )
  likes = models.IntegerField(default=0)

  class Meta:
    ordering = ['release_year']
    unique_together = ['title', 'release_year']