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

    class Meta:
        db_table = 'movie'

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'genre'

class MovieGenreRelation(models.Model):
    movie = models.ForeignKey(Movie)
    genre = models.ForeignKey(Genre)

    class Meta:
        db_table = 'movie_genre_relation'
