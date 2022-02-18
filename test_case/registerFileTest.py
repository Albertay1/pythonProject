import ddt

from file_register.BaseTestCase import BaseTest

from file.readerTest import reader


@ddt.ddt
class SegisterTestFile(BaseTest):
    table = reader("register_test.csv")

    @ddt.data(*table)
    def test_register(self, row):
        self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=reg")
        self.driver.find_element('name', 'username').send_keys(row[0])
        self.driver.find_element('name', 'password').send_keys(row[1])
        self.driver.find_element('name', 'userpassword2').send_keys(row[2])
        self.driver.find_element('name', 'mobile_phone').send_keys(row[3])
        self.driver.find_element('name', 'email').send_keys(row[4])
        # self.driver.find_element_by_class_name("reg_btn").click()
