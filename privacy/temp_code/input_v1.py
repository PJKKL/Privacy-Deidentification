#파일 이름을 직접 입력받는 함수
import csv
import sys
import os

"""
#파일 디렉토리를 만드는 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
"""


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


with open(abs_dir + f_name, 'r') as csvfile:
    #csv 파일에서 line들을 읽어서 list로 저장하기
    #저장하는 temp 리스트 이름은 input
    rdf = csv.reader(csvfile)
    for line in rdf:
        data_arr.append(line)

    #인풋들의 열 개수 파악
    column = data_arr[0]
    column_count = len(column)
    print("총 열 개수는 {}입니다.".format(column_count))
    print(column, end="\n\n")
    #데이터 정제를 위해 첫 번째 열에 위치한 column name들을 분리
    del data_arr[0]

    #예외처리 조건 수정 필요
    if len(data_arr) <= 1 and len(data_arr[0]):
        print("빈 csv파일입니다.")
    else: 
        print("전체 데이터 셋")
        for line in data_arr:
            print(line)
