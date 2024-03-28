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
H, W = map(int, input().split())
X = [0] * (H)
Z = [[0]*(W + 1) for i in range(H+1) ]
for i in range(H):
	X[i] = list(map(int, input().split()))


Q = int(input())
A,B,C,D = [0]*Q,[0]*Q,[0]*Q,[0]*Q
for i in range(Q):
    A[i],B[i],C[i],D[i] = map(int,input().split())

# 横方向に累積和
for i in range(1,H+1):
     for j in range(1,W+1):
        Z[i][j] = Z[i][j-1] + X[i-1][j-1]

# 縦方向に累積和
for i in range(1,W+1):
    for j in range(1,H+1):
        Z[j][i] = Z[j-1][i] + Z[j][i]

for i in range(Q):
     print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] - Z[C[i]][B[i]-1])
