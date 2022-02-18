import csv
import os


def reader(filename):
    list = []
    # path = '../test_date/' + filename
    base_path = os.path.dirname(__file__)
    path = base_path.replace("file", "test_date/" + filename)
    # file = open(path)
    with open(path) as file:
        table = csv.reader(file)
        i = 0
        for row in table:
            if i == 0:
                pass
            else:
                list.append(row)
            i = i + 1
    return list
