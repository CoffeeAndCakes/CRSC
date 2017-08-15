import sys
import os
import django
import csv

datasets_path = "../datasets/movie_lens/ml-latest-small/"

def setup():
    # django の設定を使えるようにする
    current_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.join(current_path, '../'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
    django.setup()

def movies():
    from movies.models import Movie
    Movie.objects.all().delete()

    reader = csv.reader(open(datasets_path + "movie-years.csv"), delimiter="\t")
    next(reader) # header skip

    for row in reader:
        movie = Movie()
        movie.id = row[0]
        movie.english_title = row[1]
        movie.year = row[3]
        movie.save()

if __name__ == '__main__':
    setup()
    movies()
