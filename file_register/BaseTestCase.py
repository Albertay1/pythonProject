import time

import unittest2
from selenium import webdriver


class BaseTest(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
