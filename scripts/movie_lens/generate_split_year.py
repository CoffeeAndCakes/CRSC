import csv
import re

path = './datasets/movie_lens/ml-latest-small/movies.csv'

with open(path, 'r') as f:
    all    = csv.reader(f)
    header = next(all)  # ヘッダーを読み飛ばしたい時
    header.append("year")
    print(",".join(header))

    for row in all:

        title = row[1]
        match = re.search("\(\d{4}\)", title)
        if match is not None:
            row[1] = row[1].replace(match.group(), "")
            row.append(match.group()[1:-1])
        else:
            row.append('0')

        txt = "\t".join(row)
        print(txt)
