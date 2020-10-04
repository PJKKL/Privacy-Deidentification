import pandas as pd
import numpy as np
# scikit-learn 모듈 설치 필요
# pip install scikit-learn || conda install scikit-learn
import sklearn

#잡음 추가
def noise_add(df):
    num_list = []
    # 난수 생성 시작점
    start = int(input("start: "))
    # 난수 생성 종료점
    end = int(input("end: "))

    for row in df:
        row += randint(start, end)
        num_list.append(row)
    return num_list


#순열 치환
#전체 df를 받아옴
def df_permutation (df):

    name_list = []
    final = pd.DataFrame()
		
		# 기준점이 될 column 해당 Dataset에서 시도 에 해당
    col_name = input("column name: ")
		# permutation 대상 column 해당 Dataset에서 월 소득에 해당
    target = input("change value: ")

		# series에 있는 모든 종류의 이름들을 name_list에 저장
    for row in df[col_name]:
        if row not in name_list:
            name_list.append(row)

    for name in name_list:
				# 사용자에게 입력받은 column이름에 해당하는 내용만 temp에 저장
        temp_df = df[df[col_name] == name]
        temp = temp_df[target]

				# temp의 Data들을 랜덤하게 배치
        temp=sklearn.utils.shuffle(temp).reset_index(drop=True)

				# 여기서 new_df를 temp_df.copy()로 카피하는 이유는 SettingWithCopyWarning이 발생했기 때문
				# temp series를 list로 바꾸지 않으면 NaN값이 데이터 프레임에 추가됨(이유를 모르겠어서 리스트로 사용)
        val_list = temp.values.tolist()
        new_df = temp_df.copy()
        new_df[target + ' 변경 후'] = val_list

				# final Dataframe에 결과를 차근차근 저장
				# 이부분에서 자동으로 col_name에 의한 sorting이 발생함
        final = pd.concat([final, new_df], ignore_index = True)

    return final

# 토큰화
def token_maker(len):
    #string_pool = string.ascii_lowercase # 소문자
    string_pool = string.ascii_uppercase # 대문자
    result = "" # 결과 값
    for i in range(len) :
     result += choice(string_pool) # 랜덤한 문자열 하나 선택
    return result

def tokenizer(df):
    word_list = []
    word_before = int(input("start: "))
    word_after = int(input("finish: "))
    len = int(input("length: "))  # 토큰 길이

    for row in df:
        token = token_maker(len)
        token_table[token] = row    # 토큰 테이블 제작
        word_list.append(row[:word_before] + token + row[word_after:])
    return word_list


# 의사 난수 생성
def randommaker(num):   # num의 단위 : byte
    rand = secrets.token_hex(num)


#확인을 위한 코드
df = pd.read_csv("./dataset/monthly_income.csv", encoding="EUC-KR")

print(df)
df = df_permutation(df)
print(df)