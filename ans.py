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
os.system("clear")
with open("HandInput.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------