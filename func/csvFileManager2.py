import csv
import os.path


def csv_reader(filename):
    # path = "../test_date/" + filename
    # 下面是获取当前文件夹路径的方法：F:\pythonProject\func
    base_path = os.path.dirname(__file__)
    # 下面是将获取到的路径进行一个替换，将func替换成test_date + filename：F:\pythonProject\func - func + test_date +fliename
    # 最终得到的结果为：F:\pythonProject\test_date\register.csv
    path = base_path.replace("func", "test_date/" + filename)
    file = open(path)
    table = csv.reader(file)
    list = []
    i = 0
    for row in table:
        if i == 0:
            pass
        else:
            list.append(row)
        i = i + 1
    return list
