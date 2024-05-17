from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  release_date = models.DateField()
  overview = models.TextField()
  poster_path = models.TextField()
  vote_count = models.IntegerField()
  vote_average = models.FloatField()
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")
  hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="hate_movies")
  favorite_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="favorite_movies")
  genres = models.ManyToManyField(Genre)
  
  
  def __str__(self):
        return self.title