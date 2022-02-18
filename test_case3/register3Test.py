import ddt
import unittest2
from selenium.webdriver.common.by import By

from func.csvFileManager2 import csv_reader
from test_case3.BaseTestCase import BaseTestCase


@ddt.ddt
class Register3Test(BaseTestCase):
    table = csv_reader("register.csv")

    @ddt.data(*table)
    def test_register3(self, row):
        self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=reg")
        self.driver.find_element(By.NAME, "username").send_keys(row[0])
        self.driver.find_element(By.NAME, "password").send_keys(row[1])
        self.driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
        self.driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
        self.driver.find_element(By.NAME, "email").send_keys(row[4])
        # 不加星号，表示一个变量，就是列表本身
        print(self.table)
        # 加星号，表示四个变量，把列表中每个元素看成一个单独的变量
        print(*self.table)


if __name__ == '__main__':
    unittest2.main()
