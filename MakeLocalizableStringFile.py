import pandas as pd
import os


def write_localizable_files(localize_dict):
    for key, value in localize_dict.items():

        new_path = os.path.join(target_path, key + ".lproj")
        if not os.path.isdir(new_path):
            os.mkdir(new_path)

        fp = open(new_path + '/' + 'Localizable.strings', 'a')
        for idx, string in enumerate(value):
            if idx + 2 < min_row or idx + 2 > max_row:
                continue

            if '= "";' in string or " = " not in string:
                continue
            fp.write(string + "\n")

            add_key(new_path, string)

        print(key + "파일 생성 완료")


def add_key(new_path, string):
    with open(new_path + '/' + 'Localizable.strings', "r+") as f:
        d = f.readlines()
        f.seek(0)
        current_key = list(string.split(" = "))[0]

        for i in d:
            if '= "";' in i or " = " not in i:
                continue
            previous_key = list(i.split(" = "))[0]

            if previous_key != current_key:
                f.write(i)

        f.truncate()


# file_name = input("file name: ").rstrip()
# sheet_name = input("sheet name: ").rstrip()
# target_path = input("target path: ").rstrip()
min_row, max_row = map(int, input("text your range: ").split())

file_name = "/Users/yunjohyeon/Downloads/번역배치파일.xlsx"
sheet_name = "★번역요청"
target_path = "/Users/yunjohyeon/Downloads"


data = pd.ExcelFile(file_name).parse(sheet_name)
korean = map(str, data['Unnamed: 19'])
english = map(str, data['Unnamed: 20'])
chinese = map(str, data['Unnamed: 21'])
japanese = map(str, data['Unnamed: 22'])

localize_dict = {"ko": korean, "en": english, "zh-Hans": chinese, "ja": japanese}
write_localizable_files(localize_dict)
