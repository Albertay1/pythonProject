import ddt

from file.readerTest import reader
from file_register.BaseTestCase import BaseTest


@ddt.ddt
class Login2Test(BaseTest):
    table = reader("login_test.csv")

    @ddt.data(*table)
    def test_login2(self, row):
        self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=login")
        self.driver.find_element("name", 'username').send_keys(row[0])
        self.driver.find_element('name', 'password').send_keys(row[1])
