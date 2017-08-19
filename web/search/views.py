from django.shortcuts import render
from movies.models import Movie, Genre

def index(request):
    genres = Genre.objects.all()
    context = {'genres': genres}

    return render(request, 'search/index.html', context)

def genres_result(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.all()

    context = {
        "genre": genre,
        "movies": movies
    }
    return render(request, 'search/genres.html', context)

def years_result(request, year):
    movies = Movie.objects.filter(year=year)

    context = {
        'movies': movies,
        'year': year
    }

    return render(request, 'search/years.html', context)
