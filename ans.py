import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import copy, math, bisect
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# 存在しないkeyアクセス時デフォルト値生成
from collections import defaultdict
# リスト各要素の数え上げ 辞書型サブクラス
from collections import Counter
import io,sys,os
os.system("clear")
with open("HandInput.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------
N,A,B = map(int,input().split())
D = list(map(int,input().split()))
week = A+B
# 余りを考えて、1週間分に落とし込む
for i in range(N):
    D[i] = D[i]%week
D.sort()
# 2週分考える
# 連続するサイクルをシュミレートする
for i in range(N):
    D.append(D[i]+week)

# N個の予定が休日の範囲に収まるかどうか調べる
tmp = float('inf')
for i in range(N):
    tmp = min(tmp,D[i+N-1]-D[i]+1)
print('Yes' if tmp <= A else 'No')



# result = True
# for i in range(N):
#     if A < (D[i]%week) or D[i]%week == 0:
#         result = False
#         break
# print('Yes' if result else 'No')