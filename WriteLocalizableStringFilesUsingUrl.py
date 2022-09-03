import gspread

# https://github.com/burnash/gspread

gc = gspread.service_account()

# open a sheet
work_sheet = gc.open("★번역요청").sheet1

# getting all values from a row or a column
korean_list = work_sheet.col_values(19)
english_list = work_sheet.col_values(20)
chinese_list = work_sheet.col_values(21)
japanese_list = work_sheet.col_values(22)
