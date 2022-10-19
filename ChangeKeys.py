import pandas as pd
import os
import fileinput

"""
요구사항
- oldKey를 newKey로 교체
- ex) "common_sinsangmarket".localized(hint: "신상마켓") -> "NewKey".localized(hint: "신상마켓") 로 변경
-  


"""

file_name = "/Users/yunjohyeon/Downloads/KeyChanging.xlsx"
sheet_name = "변경"

data = pd.ExcelFile(file_name).parse(sheet_name)
previous_list = list(map(str, data['기존키값']))
current_list = list(map(str, data['바뀐키값']))
directory_path = "/Users/yunjohyeon/ssm-mobile-ios/SinsangMarket_Some"


# .swift 파일 내에서 키값들 교체
def change_key(path):
    print("### " + file_name + " 변환 시작")

    fp = open(path, 'r')
    replacement = ""
    for idx, line in enumerate(fp.readlines()):
        new_line = line
        for idx in range(0, len(previous_list)):
            if previous_list[idx] in line:
                print("** 중복 값 있음: ", previous_list[idx])
                new_line = line.replace(previous_list[idx], current_list[idx])
                print("** 변경된 값", new_line)
                break
        replacement = replacement + new_line
    fp.close()

    fout = open(path, "w")
    fout.write(replacement)
    fout.close()
    print("### " + file_name + " 변환 완료")


# 전체 swift 파일 경로 검색
for (root, dirs, files) in os.walk(directory_path):
        if len(files) > 0:
            for file_name in files:
                _, extension = file_name.split(".")
                if extension != "swift":
                    continue
                full_path = root + "/" + file_name
                # change_key(full_path)


test_file = "/Users/yunjohyeon/ssm-mobile-ios/SinsangMarket_Some/UI/MyPage/Sub/RecentlyGoods/MyPageRecentlyGoodsViewController.swift"
change_key(test_file)