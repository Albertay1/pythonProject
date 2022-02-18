# 导入csv代码库
import csv
# 指定文件获取的路径
path = r"/test_date/register_test.csv"
# 打开文件
file = open(path)
# 读取文件的内容
table = csv.reader(file)
# 打印文件内容
for row in table:
    print(row)
