from django.shortcuts import render
from movies.models import Genre

def index(request):
    genres = Genre.objects.all()
    context = {'genres': genres}

    return  render(request, 'search/index.html', context)
