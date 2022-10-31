import pandas as pd
import os

"""
요구사항 
- 모웹 통합시트의 기존 키값에 따른 번역값이 번역요청 시트의 번역값과 다른 부분이 있는지 확인할 것
"""

file_name = "/Users/yunjohyeon/Downloads/번역배치파일.xlsx"
previous_sheet = "★번역요청"
new_sheet = "모웹 통합 시트"

previous_data = pd.read_excel(file_name, sheet_name=previous_sheet, skiprows=[1, 2], usecols='G:J, T')
previous_list = previous_data.values.tolist() # 한, 영, 중, 일 순

new_data = pd.read_excel(file_name, sheet_name=new_sheet, usecols='A,D:G')
new_list = new_data.values.tolist() # 키, 한 중 영 일


def isNaN(num):
    return num != num

for n_data in new_list:
    n_key, n_ko, n_zh, n_en, n_ja = n_data
    for p_data in previous_list:
        if isNaN(p_data[-1]):
            continue

        p_ko, p_ja, p_en, p_zh, p_key = p_data
        p_key = p_key.split(" ")[0].strip("\"")
        if p_key != n_key:
            continue

        if not(p_ko == n_ko and p_zh == n_zh and p_en == n_en and p_ja == n_ja):
            print(n_key, "키 검사결과 다름")
            if p_ko != n_ko:
                print("** 한국어 ", "(이전):", p_ko, "(이후):", n_ko)
            if p_en != n_en:
                print("** 영어 ", "이전: ", p_en, "이후", n_en)
            if p_ja != n_ja:
                print("** 일본어 ", "이전: ", p_ja, "이후", n_ja)
            if p_zh != n_zh:
                print("** 중국어 ", "이전: ", p_zh, "이후", n_zh)
            print()



