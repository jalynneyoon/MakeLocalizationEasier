import pandas as pd
import os

"""
요구사항
- oldKey를 newKey로 교체
- ex) "common_sinsangmarket".localized(hint: "신상마켓") -> "NewKey".localized(hint: "신상마켓") 로 변경
"""

# file_name = input("file name: ").rstrip()
# sheet_name = input("sheet name: ").rstrip()
# directory_path = input("target path: ").rstrip()
file_name = "/Users/yunjohyeon/Downloads/번역배치파일.xlsx"
sheet_name = "모웹 통합 시트"

data = pd.ExcelFile(file_name).parse(sheet_name)
print(data)
previous_list = list(map(str, data['모바일 키']))
current_list = list(map(str, data['key']))
directory_path = "/Users/yunjohyeon/ssm-mobile-ios/SinsangMarket_Some"


# .swift 파일 내에서 키값들 교체
def change_key(path):
    file_name = path.split("/")[-1]
    print(file_name + " 파일 확인")

    fp = open(path, 'r')
    replacement = ""
    for idx, line in enumerate(fp.readlines()):
        new_line = line
        for idx in range(0, len(previous_list)):
            if '\"' + previous_list[idx] + '\"' in line:
                print("** 중복 값 있음: ", previous_list[idx])
                new_line = line.replace(previous_list[idx], current_list[idx])
                print("** 변경된 값: ", new_line.lstrip())
                break
        replacement = replacement + new_line
    fp.close()

    fout = open(path, "w")
    fout.write(replacement)
    fout.close()


# 전체 swift 파일 경로 검색
for (root, dirs, files) in os.walk(directory_path):
        if len(files) > 0:
            for file_name in files:
                _, extension = file_name.split(".")
                if extension != "swift":
                    continue
                full_path = root + "/" + file_name
                change_key(full_path)


# test_file = "/Users/yunjohyeon/ssm-mobile-ios/SinsangMarket_Some/UI/MyPage/Sub/RecentlyGoods/MyPageRecentlyGoodsViewController.swift"
# change_key(test_file)