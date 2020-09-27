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
    print(file_nms)

data_arr = list()
column = list()
column_count = list()

"""
1. data_arr = csv 파일 데이터를 저장하는 배열. 3차원 리스트
2. column = csv 파일의 첫번째 행을 저장하는 배열 -> 열의 이름. 2차원 리스트
3. column_count = 열 이름의 개수를 저장하는 배열 -> 열 이름의 개수. 1차원 리스트
"""

for i in range(len(file_nms)):
    #추출 중인 파일 이름 표시
    f_name = file_nms[i]
    print(file_nms[i])

    #디렉토리 path 기준으로 모든 csv 파일들을 다 가져오기
    with open(abs_dir + f_name, 'r') as csvfile:
        #csv 파일에서 line들을 읽어서 list로 저장하기
        #저장하는 temp 리스트 이름은 input
        rdf = csv.reader(csvfile)
        for line in rdf:
            data_arr[i].append(line)

        #인풋들의 열 개수 파악
        column.append(data_arr[i][0])
        column_count.append(len(column[i]))
        print("총 열 개수는 {}입니다.".format(column_count[i]))
        print(column[i], end="\n\n")
        #데이터 정제를 위해 첫 번째 열에 위치한 column name들을 분리
        del data_arr[i][0]



        """
        if len(data_arr) <= 1 and len(data_arr[0]):
            print("빈 csv파일입니다.")
        else: 
            print("전체 데이터 셋")
            for line in data_arr:
                print(line)
        """


