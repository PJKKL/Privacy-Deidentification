#파일 디렉토리 안의 csv 파일을 모두 가져오는 함수
import csv
import sys
import os

"""
#파일 디렉토리를 만드는 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
"""

#파일 이름들 가져오기
folder_name = 'dataset/'
abs_dir = os.path.join(os.getcwd(), folder_name)


file_nms = os.listdir(abs_dir)
#디렉토리안에 파일이 없을 경우 예외 처리
if len(file_nms) == False:
    print("해당 경로에 아무 파일도 존재하지 않습니다.")
    exit(1)
else:
    print("해당 경로에 존재하는 파일 목록")
    print(file_nms, end = "\n\n")

data_arr = list()

for f_name in file_nms:
    #추출 중인 파일 이름 표시
    print(f_name, end = "\n\n")

    #data배열을 초기화
    data_arr = []

    #디렉토리 path 기준으로 모든 csv 파일들을 다 가져오기
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

        #조건 수정 필요
        if len(data_arr) <= 1:
            print("빈 csv파일입니다.")
        else: 
            print("전체 데이터 셋")
            for line in data_arr:
                print(line)

        print()




