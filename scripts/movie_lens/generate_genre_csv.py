import csv
head = "movieId,genre"
path = './datasets/movie_lens/ml-latest-small/movies.csv'
print(head)
with open(path, 'r') as f:
    all    = csv.reader(f)
    header = next(all)  # ヘッダーを読み飛ばしたい時

    for row in all:
        genres = row[2].split('|')
        if genres[0] == "(no genres listed)":
            break
        for genre in genres:
            print(row[0] + "," + genre)          # 1行づつ取得できる
