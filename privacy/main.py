#main 함수

import pandas as pd
import csv
import sys
import os
import time
from pandas import DataFrame
from generalization import *
from randomized import *
from statistical_processing import *


#csv 데이터 입력

def input_csv():
    #csv 데이터들의 path
    folder_name = 'dataset/'
    abs_dir = os.path.join(os.getcwd(), folder_name)

    #파일 이름을 직접 입력받기
    f_name = input("파일 이름을 입력해주세요: ")
    data_arr = list()

    file_path = abs_dir + f_name

    #df 로 가져오기
    df = pd.read_csv(file_path, encoding="euc-kr")

    return df

def output_csv(df):
    #조치 완료 된 csv 파일 추출하기

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

    df.to_csv(res_dir + '/dataresult.csv', sep=',', encoding="euc-kr")

df = input_csv()
output_csv(df)



"""
데이터셋 별 조치
"""


