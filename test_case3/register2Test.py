from selenium.webdriver.common.by import By

from func.csvFileManager2 import csv_reader
from test_case3.BaseTestCase import BaseTestCase


class register2Test(BaseTestCase):
    def test_register2(self):
        table = csv_reader("register.csv")
        for row in table:
            self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=reg")
            self.driver.find_element(By.NAME, "username").send_keys(row[0])
            self.driver.find_element(By.NAME, "password").send_keys(row[1])
            self.driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
            self.driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
            self.driver.find_element(By.NAME, "email").send_keys(row[4])
            # self.driver.find_element(By.CLASS_NAME, "reg_btn").click()