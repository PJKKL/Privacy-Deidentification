#리스트를 csv 파일로 추출하기
import csv
import os
import sys
import time

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


data = [['F', '25', '경기', '2700'],
['M', '30', '경기', '3900'],
['M', '40', '서울', '2400'],
['F', '41', '서울', '2500'],
['M', '45', '서울', '2600'],
['F', '37', '강원', '2800'],
['F', '29', '경상', '2700'],
['M', '49', '전라', '1200'],
['M', '33', '제주', '1900'],
['M', '36', '제주', '2500'],
['M', '15', '서울', '1200'],
['M', '16', '광주', '1300'],
['M', '17', '부산', '2000'],
['M', '18', '제주', '2100'],
['M', '19', '서울', '2200'],
['M', '55', '광주', '2300'],
['M', '56', '부산', '2100'],
['M', '57', '제주', '1400'],
['M', '58', '서울', '1800'],]

f = open('write.csv', 'w', newline="")
wr = csv.writer(f)
wr.writerow(data)


with open(res_dir + '/dataresult.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    for line in data:
        writer.writerow(line)
