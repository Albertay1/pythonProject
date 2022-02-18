from selenium.webdriver.common.by import By

from test_case3.BaseTestCase import BaseTestCase


class registerTest(BaseTestCase):
    def test_register(self):
        self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=reg")
        self.driver.find_element(By.NAME, "username").send_keys("albert")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        self.driver.find_element(By.NAME, "mobile_phone").send_keys("15255213636")
        self.driver.find_element(By.NAME, "email").send_keys("12345678985@11.com")
        self.driver.find_element(By.CLASS_NAME, "reg_btn").click()
