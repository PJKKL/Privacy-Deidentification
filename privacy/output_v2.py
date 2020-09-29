#using pandas read csv file

import pandas as pd
import csv
import sys
import os
import time
from pandas import DataFrame


data = {'ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
        'X1': [1, 2, 3, 4, 5],
        'X2': [3.0, 4.5, 3.2, 4.0, 3.5]
}


data_df = DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

#DataFrame print -> 확인용으로 이후 삭제 가능
print(data_df)


#현재 디렉토리
abs_dir = os.path.join(os.getcwd(), "result/")
#result 디렉토리: 결과물 저장 디렉토리
res_dir = abs_dir

#결과 파일을 저장하는 디렉토리 이름을 현재 시간으로 설정
#결과 디렉토리 paht 생성
name = str(time.strftime('%y%m%d-%H%M%S'))
if os.path.isdir(abs_dir):
    res_dir = res_dir + name
    os.makedirs(res_dir)
else:
    res_dir = res_dir + name
    os.makedirs(res_dir)

data_df.to_csv(res_dir + '/dataresult.csv', sep=',')

