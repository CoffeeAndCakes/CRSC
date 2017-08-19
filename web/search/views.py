from django.shortcuts import render
from movies.models import Movie, Genre

def index(request):
    genres = Genre.objects.all()
    context = {'genres': genres}

    return render(request, 'search/index.html', context)

def years_result(request, year):
    movies = Movie.objects.filter(year=year)

    context = {
        'movies': movies,
        'year': year
    }

    return render(request, 'search/years.html', context)
