import pandas as pd
import sys
import os

file_name, sheet_name = sys.stdin.readline().split()
targetPath = sys.stdin.readline().strip("\n")

data = pd.ExcelFile(file_name).parse(sheet_name)
korean = map(str, data['Unnamed: 19'])
english = map(str, data['Unnamed: 20'])
chinese = map(str, data['Unnamed: 21'])
japanese = map(str, data['Unnamed: 22'])

localize_dict = {"ko": korean, "en": english, "zh-Hans": chinese, "ja": japanese}

for key, value in localize_dict.items():

    new_path = os.path.join(targetPath, key + ".lproj")
    if not os.path.isdir(new_path):
        os.mkdir(new_path)

    fp = open(new_path + '/' + 'Localizable.strings', 'w')
    for string in value:
        if '= "";' in string or "=" not in string:
            continue
        fp.write(string + "\n")

    print(key + "파일 생성 완료")


