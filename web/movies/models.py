from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    english_title = models.CharField(max_length=200)
    japanese_title = models.CharField(max_length=200)
    year = models.IntegerField()
    imdb_link = models.TextField()
    tmd_link = models.TextField()
    image_url = models.TextField()
