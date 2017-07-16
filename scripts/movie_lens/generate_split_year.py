import csv
import re

path = './datasets/movie_lens/ml-latest-small/movies.csv'

with open(path, 'r') as f:
    all    = csv.reader(f)
    header = next(all)  # ヘッダーを読み飛ばしたい時
    print(header)

    for row in all:
        title = row[1]
        year = re.search("\(\d{4}\)", title)
        if year == None
        else:
            print(year.group()[1:-1])
