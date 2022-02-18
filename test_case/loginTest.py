import time

from file.readerTest import reader
from file_register.BaseTestCase import BaseTest


class LoginTest(BaseTest):
    def test_Login(self):
        # table = reader("login_test.csv")
        # for row in table:
        self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=login")
        self.driver.find_element('id', 'username').send_keys("ray1")
        self.driver.find_element('id', 'password').send_keys("123456")
        self.driver.find_element_by_css_selector(".login_btn.fl").click()
        time.sleep(3)
        print(self.driver.title)
        print(self.driver.current_url)
        welcome = self.driver.find_element_by_css_selector(".site-nav-right.fr > a:nth-child(1)").text
        print(welcome)
        search = self.driver.find_element_by_css_selector(".btn1").get_attribute("value")
        print(search)
        self.assertEqual("我的会员中心 - 道e坊商城 - Powered by Haidao", self.driver.title)
        self.assertEqual("http://129.211.129.101:9007/index.php?m=user&c=index&a=index", self.driver.current_url)
        self.assertEqual('你好 ray', welcome)
