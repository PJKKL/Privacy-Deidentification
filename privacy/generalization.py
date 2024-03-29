import math
import pandas as pd
import numpy as np
from random import randint


# float유형을 반올림해서 int로 변경하는 함수
def df_round_float_to_int(df):
    return df.astype(int)

# 일반 반올림 기법, df는 데이터 프레임, num은 자리 수
# 0 -> 1의 자리, -1 -> 10의 자리
def general_round(df, num):
    df = df.round(num)
    return df

# 일반 올림 기법, df는 데이터 프레임, num은 자리 수
# 0 -> 1의 자리, -1 -> 10의 자리
def general_ceil(df, num):
    num_list = []

    for row in df:
        num_list.append(math.ceil(row / 10 ** (-1 * num)) * 10 ** (-1 * num))
    
    return pd.DataFrame(num_list)

# 일반 내림 기법, df는 데이터 프레임, num은 자리 수
# 0 -> 1의 자리, -1 -> 10의 자리
def general_floor(df, num):
    num_list = []

    for row in df:
        num_list.append(math.floor(row / 10 ** (-1 * num)) * 10 ** (-1 * num))
    
    return pd.DataFrame(num_list)


# random rounding 구현을 위해서 끌어온 함수
def df_max(df):
    return df.max(axis = 0, skipna = True)
def df_min(df):
    return df.min(axis = 0, skipna = True)

# random 라운딩
def df_random_rounding(df):
    temp_min = len(str(df_min(df)))

    #랜덤한 자리수를 구함 (0부터 가장 작은 값의 자리 수 까지)
    #예를 들어 100, 230, 1000, 12349, 203 이라는 데이터가 들어있다면 최소 값 100의 자리수(3)이 temp_min으로 들어감
    #따라서 라운딩 조치를 취해줄 값은 0 ~ 2 사이에서 랜덤하게 선택되어 rand_num으로 들어감
    rand_num = randint(0, temp_min - 1) 

    #어떤 라운딩 조치를 취할 것인지를 골라주는 랜덤 플래그
    op = randint(0, 2)

    if op == 0:
        return general_round(df, -1 * rand_num)
    elif op == 1:
        return general_ceil(df, -1 * rand_num)
    else:
        return general_floor(df, -1 * rand_num)


#def control_rounding():

# 문자를 바꿔주는 replace 함수
def df_char_replace(df):
    word_before = input("word before: ")
    word_after = input("word after: ")
    
    return df.str.replace(pat = word_before, repl = word_after, regex = False)


# 마스킹 처리를 하는 함수       
def df_masking(df):
    masking_start = int(input("masking start(nun): "))
    masking_end = int(input("masking end(num): "))
    masking_symbol = input("masking symbol: ")
    
    return df.str.slice_replace(start = masking_start, stop = masking_end, repl = masking_symbol)


#문자열 mapping 상위 개념으로 범주화
def df_mapping(df):
    df_map = dict()
    key = None

    while(True):
        key = input('key: ')
        if key == '-1':
            break
        value = input('value: ')

        df_map[key] = value

    df = df.map(df_map)

    key = input('NaN value to : ')
    
    return df.replace(np.nan, key)


