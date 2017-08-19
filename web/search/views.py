from django.shortcuts import render
from movies.models import Movie, Genre, MovieGenreRelation

def index(request):
    genres = Genre.objects.all()
    context = {'genres': genres}

    return render(request, 'search/index.html', context)

def genres_result(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.filter(moviegenrerelation__genre_id=genre_id)

    context = {
        "genre": genre,
        "movies": movies
    }
    return render(request, 'search/genres.html', context)

def years_result(request, year):
    start = int(year)
    end = int(year) + 9
    movies = Movie.objects.filter(year__gte=start, year__lte=end)

    context = {
        'movies': movies,
        'year': year
    }

    return render(request, 'search/years.html', context)

def keyword_result(request):
    q = request.GET.get('q')
    movies = Movie.objects.filter(english_title__contains=q)

    context = {
        'movies': movies,
        'keyword': q
    }
    return render(request, 'search/keyword.html', context)
