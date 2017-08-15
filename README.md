# Recommendation

## いろいろな資料はwikiにまとめる
https://github.com/CoffeeAndCakes/recommendation/wiki

## データの準備
使用するデータセットは `datasets/` に配置する。
自前でダウンロードしてもよいがスクリプトも用意してある

### MovieLens
```sh
$ scripts/fetch_movie_lens.sh
```

---

## 開発環境構築

下記コマンドを打ち込むとシステムのPythonとは別のPythonの環境をこのプロジェクト用に作成されます。

```sh
# このリポジトリのトップ
$ cd recommendation

# システムのpythonと切離した環境を作成  
$ python -m venv .

# 上記で作成したpython環境を使えるようにアクティベートします
$ source ./bin/activate

# 開発に必要なライブラリをインストールします
$ pip install -r requirements.txt
```

## DB 投入用データ作成
```sh
# このリポジトリのトップ
$ cd recommendation

# movie_lensのデータをダウンロードする
# ダウンロード済みならスキップしてよい
$ scripts/fetch_movie_lens.sh

$ python scripts/movie_lens/generate_split_year.py >  ./datasets/movie_lens/ml-latest-small/movie-years.csv
$ python scripts/movie_lens/generate_genre_csv.py >  ./datasets/movie_lens/ml-latest-small/genres.csv
```

## DB構築

```sh
# django の project の root に移動
$ cd recommendation/web

# create table
$ python manage.py migrate

# 初期データ投入
$ python db/seed.py
```
