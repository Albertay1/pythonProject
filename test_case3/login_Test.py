import time

import unittest2
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_case3.BaseTestCase import BaseTestCase


class LoginTest(BaseTestCase):

    def test_login(self):
        self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=login")
        self.driver.find_element(By.NAME, "username").send_keys("ray1")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, ".login_btn.fl").click()
        time.sleep(3)
        # 获取a标签的文本信息，并转化为text文本信息，并打印
        welcome = self.driver.find_element(By.CSS_SELECTOR, ".site-nav-right.fr > a:nth-child(1)").text
        print(welcome)
        # 获取当前页面的URL地址信息
        print(self.driver.current_url)
        # 获取当前页面的title
        print(self.driver.title)
        # 获取界面上btn1对应元素的value属性
        search = self.driver.find_element(By.CSS_SELECTOR, ".btn1").get_attribute("value")
        print(search)
        # 添加断言判断
        self.assertEqual("您好 ray1", welcome)
        self.assertEqual("http://129.211.129.101:9007/index.php?m=user&c=index&a=index", self.driver.current_url)
        self.assertEqual("我的会员中心 - 道e坊商城", self.driver.title)
        self.assertEqual("搜索", search)
