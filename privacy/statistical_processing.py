import math
import pandas as pd
import numpy as np
from random import randint

# 최대 값
def df_max(df):
    return df.max(axis = 0, skipna = True)

# 최소 값
def df_min(df):
    return df.min(axis = 0, skipna = True)

# 평균
def df_average(df):
    return df.mean(axis = 0, skipna = True)

# 중앙 값
# median은 numpy_array의 메소드가 아니라 numpy의 메소드임    
def df_median(df):
    return np.median(df)

# 표준 편차
def df_std(df):
    return df.std(axis = 0, skipna = True)

# 분산
def df_var(df):
    return df.var(axis = 0, skipna = True)

