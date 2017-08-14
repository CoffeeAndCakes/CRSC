from django.http import Http404
from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return  render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("movie does not exist")
    return render(request, 'movies/detail.html', {'movie': movie})
