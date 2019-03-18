import xlrd
from test import translate

data=xlrd.open_workbook('webAPI.xls')  # 打开xls文件
print (data.sheet_names())
table=data.sheet_by_index(0)  # 打开第一张表
nrows=table.nrows   # 获取表的行数
for i in range(100):
    print(translate(table.row_values(i)[0]))
    print(translate(table.row_values(i)[1]))