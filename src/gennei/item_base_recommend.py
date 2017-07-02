import numpy as np
import pandas as pd

# ref: http://qiita.com/kotaroito/items/6acb58bb16b68a460af9

def compute_item_similarities(R):
    # n: movie counts
    n = R.shape[1]
    sims = np.zeros((n,n))

    for i in range(n):
        for j in range(i, n):
            if i == j:
                sim = 1.0
            else:
                # R[:, i] は アイテム i に関する全ユーザの評価を並べた列ベクトル
                sim = similarity(R[:,i], R[:,j])
            sims[i][j] = sim
            sims[j][i] = sim
    return sims

def similarity(item1, item2):
    # item1 と item2 のどちらも評価済であるユーザの集合
    common = np.logical_and(item1 != 0, item2 != 0)

    v1 = item1[common]
    v2 = item2[common]

    sim = 0.0
    # 共通評価者が 2以上という制約にしている
    if v1.size > 1:
        sim = 1.0 - cosine(v1, v2)

    return sim

def predict(u, sims):
    # 未評価は0, 評価済は1となるベクトル。normalizersの計算のために。
    x = np.zeros(u.size)
    x[u > 0] = 1

    scores      = sims.dot(u)
    normalizers = sims.dot(x)

    prediction = np.zeros(u.size)
    for i in range(u.size):
        # 分母が 0 になるケースと評価済アイテムは予測値を 0 とする
        if normalizers[i] == 0 or u[i] > 0:
            prediction[i] = 0
        else:
            prediction[i] = scores[i] / normalizers[i]

    # ユーザ u のアイテム i に対する評価の予測
    return prediction

path = "datasets/movie_lens/ml-latest-small/ratings.csv"
df   = pd.read_csv(path)
shape = (df.max().ix['userId'], df.max().ix['movieId'])
R = np.zeros(shape)
sims = compute_item_similarities(R)
