from file_register.BaseTestCase import BaseTest


class registerTest(BaseTest):
    def test_segister(self):
        self.driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=reg")
        self.driver.find_element('name', 'username').send_keys("yubanghui1")
        self.driver.find_element('name', 'password').send_keys("123456")
        self.driver.find_element('name', 'userpassword2').send_keys("123456")
        self.driver.find_element('name', 'mobile_phone').send_keys("18211111111")
        self.driver.find_element('name', 'email').send_keys("1811111111@163.com")
        self.driver.find_element_by_class_name("reg_btn").click()
