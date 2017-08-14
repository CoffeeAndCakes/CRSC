#!/usr/bin/env python
import sys
import os
import django
import csv

def setup():
    # django の設定を使えるようにする
    current_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.join(current_path, '../'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
    django.setup()

def movies():
    from movies.models import Movie
    print("import start")

if __name__ == '__main__':
    setup()
    movies()
