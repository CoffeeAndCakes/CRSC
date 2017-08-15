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
        movie = Movie(
            id=row[0],
            english_title=row[1],
            year=row[3]
        )
        movie.save()

def genres():
    from movies.models import Movie, Genre, MovieGenreRelation
    Genre.objects.all().delete()
    reader = csv.reader(open(datasets_path + "genres.csv"))
    next(reader) # header skip

    for row in reader:
        if not Genre.objects.filter(name=row[1]).exists():
            genre = Genre(
                name=row[1]
            )
            genre.save()

if __name__ == '__main__':
    setup()
    movies()
    genres()
