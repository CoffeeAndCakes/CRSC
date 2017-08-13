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
# システムのpythonと切離した環境を作成  
$ python -m venv . 

# 上記で作成したpython環境を使えるようにアクティベートします
$ source ./bin/activate

# 開発に必要なライブラリをインストールします
$ pip install -r requirements.txt
```

