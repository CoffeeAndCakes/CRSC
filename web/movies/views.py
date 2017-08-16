from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Movie

def index(request):
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 25)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return  render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("movie does not exist")
    return render(request, 'movies/detail.html', {'movie': movie})
