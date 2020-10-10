#using pandas read csv file

import pandas as pd
import csv
import sys
import os
from pandas import DataFrame

#csv 데이터들의 path
folder_name = 'dataset/'
abs_dir = os.path.join(os.getcwd(), folder_name)


#파일 이름을 직접 입력받기
f_name = input("파일 이름을 입력해주세요: ")
data_arr = list()

#없는 파일이름을 input 했을 경우의 예외 처리

try:
    fin = open(abs_dir + f_name, 'r')
except:
    print("해당 파일이 존재하지 않습니다.")
    exit(1)

file_path = abs_dir + f_name

data = pd.read_csv(file_path, encoding="euc-kr")

print(data)

