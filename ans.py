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
# "abc...xyz"
from string import ascii_lowercase 
# sortされた各データ構造を作るモジュールsortedcontainers
from sortedcontainers import SortedDict,SortedList,SortedSet
os.system("clear")
with open("HandInput.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------
def count_black_cells(A, B, C, D):
    def count_in_rectangle(x1, y1, x2, y2):
        """特定の矩形範囲で黒マスの数を計算する関数"""
        count = 0
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x + y) % 2 == 0:  # 黒マスの条件
                    count += 1
        return count
    
    # 全体の黒マスを計算
    total_black = count_in_rectangle(A, B, C, D)
    return total_black

# ユーザー入力を取得
A, B, C, D = map(int, input().split())

# 結果の出力
print(count_black_cells(A, B, C, D))
