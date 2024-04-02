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
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 動的計画法
dp = [0]*(N+1)
dp[2] = A[0]
for i in range(3,N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# 答えの復縁
# 変数placeは現在位置(ゴールから逆算してく)
ans = []
place = N
while True:
    ans.append(place)
    if place == 1:
        break
    if dp[place] == dp[place-1]+A[place-2]:
        place -= 1
    else:
        place -= 2
ans.reverse()

print(len(ans))
print(*ans)