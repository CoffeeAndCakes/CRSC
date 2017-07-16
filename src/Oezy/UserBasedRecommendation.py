import os
import math
import numpy as np
import pandas as pd
import argparse

directory = "../../datasets/movie_lens/ml-latest-small/"
dataset_name = "ratings.csv"
movies_name = "movies.csv"

dataset_file = os.path.join(directory, dataset_name)
movies_file = os.path.join(directory, movies_name)

parser = argparse.ArgumentParser(description='Input User ID and Number of recommend you want')
parser.add_argument('--user_id', action='store', type=int, required=True, metavar='User ID')
parser.add_argument('--number', action='store', type=int, required=True, metavar='Number of recommend you want')

args = parser.parse_args()

user_id = args.user_id
num = args.number


"""
step① そのユーザと他のユーザの **類似度** を計算する
↓
step② 他のユーザが見た映画のうち、ユーザAがまだ見てない映画の集合を抽出する
↓
step③ それらの映画群のうち、おすすめ度が高い映画のリストを返す。
       この選定の際に、類似度が高いユーザが見た映画ほど重みが高くなるようにする
"""


def prepare_dataset(filename):
    df = pd.read_csv(filename)
    del df["timestamp"]
    dict = {}
    userlist = df["userId"].unique()
    for k in userlist:
        df_k = df[df.userId == k]
        df_k = df_k.drop("userId", axis=1)
        dict_dayo = {}
        for i, row in df_k.iterrows():
            dict_dayo.update({row["movieId"]: row["rating"]})
        dict.update({k: dict_dayo})
    return df, dict


def get_similairty(person1, person2):

  ## 両者とも見た映画の集合を取る
  set_person1 = set(dataset[person1].keys())
  set_person2 = set(dataset[person2].keys())
  set_both = set_person1.intersection(set_person2)

  if len(set_both)==0: #共通でみた映画がない場合は類似度を0とする
    return 0

  list_destance = []

  for item in set_both:
    # 同じ映画のレビュー点の差の2乗を計算
    # この数値が大きいほど「気が合わない」=「似ていない」と定義できる
    distance = pow(dataset[person1][item]-dataset[person2][item], 2)
    list_destance.append(distance)

  return 1/(1+math.sqrt(sum(list_destance))) #各映画の気の合わなさの合計の逆比的な指標を返す


def get_recommend(person, top_N):

  totals = {} ; simSums = {} #推薦度スコアを入れるための箱を作っておく

  # 自分以外のユーザのリストを取得してFor文を回す
  # -> 各人との類似度、及び各人からの（まだ本人が見てない）映画の推薦スコアを計算するため
  list_others = dataset.keys() ; list(list_others).remove(person)

  for other in list_others:
    # 本人がまだ見たことが無い映画の集合を取得
    set_other = set(dataset[other]); set_person = set(dataset[person])
    set_new_movie = set_other.difference(set_person)

    # あるユーザと本人の類似度を計算(simは0~1の数字)
    sim = get_similairty(person, other)

    # (本人がまだ見たことがない)映画のリストでFor分を回す
    for item in set_new_movie:

      # "類似度 x レビュー点数" を推薦度のスコアとして、全ユーザで積算する
      totals.setdefault(item,0)
      totals[item] += dataset[other][item]*sim

      # またユーザの類似度の積算値をとっておき、これで上記のスコアを除する
      simSums.setdefault(item,0)
      simSums[item] += sim

  rankings = [(total/simSums[item],item) for item,total in totals.items()]
  rankings.sort()
  rankings.reverse()

  return [i[1] for i in rankings][:top_N]



df, dataset = prepare_dataset(dataset_file)
movies = pd.read_csv(movies_file)
user_movie = df[df.userId == user_id]["movieId"].tolist()
wathced = movies[movies["movieId"].isin(user_movie)]["title"]
print("Watched Movies: ")
print(wathced)

recommend = get_recommend(user_id, num)
print("Recommended Movies: ")
for n in range(num):
    item = movies[movies.movieId == recommend[n]]
    print(item)
