import csv

# 获取文件路径
path = r"F:\pythonProject\test_date\register.csv"
# 打开文件
file = open(path)
# 使用csv方法获取文件中的内容，并通过for循环打印出文件的内容
table = csv.reader(file)
for row in table:
    print(row)