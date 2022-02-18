import time

import unittest2
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://129.211.129.101:9007/index.php?m=admin&c=public&a=login")
driver.maximize_window()
driver.implicitly_wait(10)
# 输入用户名、密码和验证码，点击登录按钮
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "userpass").send_keys("password")
driver.find_element(By.NAME, "userverify").send_keys("1234")
driver.find_element(By.CLASS_NAME, "Btn").click()
# 切换至商品管理，选择添加商品界面
driver.find_element(By.LINK_TEXT, "商品管理").click()
driver.find_element(By.LINK_TEXT, "添加商品").click()
# 把selenium切换到子页面中
driver.switch_to.frame("mainFrame")
# 输入需要添加的商品名称
driver.find_element(By.NAME, "name").send_keys("iphone xs max")
# 选择商品的对应属性
driver.find_element(By.ID, "1").click()
driver.find_element(By.ID, "2").click()
driver.find_element(By.ID, "6").click()
# 使用ActionChains方法，实现双机选择一个元素
ActionChains(driver).double_click(driver.find_element(By.ID, "7")).perform()
# 使用Select方法对选择框进行定位
brand = driver.find_element(By.NAME, "brand_id")
Select(brand).select_by_value("1")

# 再次选择添加商品

# driver.find_element(By.LINK_TEXT, "添加商品").click()
# 选择商品图册按钮
driver.find_element(By.LINK_TEXT, "商品图册").click()
# 通过CSS_SELECT祖父和子孙元素的关系方式进行定位
time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#filePicker label").click()
# rt_rt_1frr1q0qhn0q1da9134215uf2q98 > label
# 使用文件上传相关的控件特点，直接针对file类型进行输入上传
driver.find_element(By.NAME, "file").send_keys("F:/LOGO/PNG/AE.png")
# 点击开始上传按钮，上传需要的文件
driver.find_element(By.CSS_SELECTOR, ".uploadBtn.state-finish.state-ready").click()
# 上传成功后再针对alert弹窗框进行处理
WebDriverWait(driver, 20, 0.5).until(expected_conditions.alert_is_present())
driver.switch_to.alert.accept()
# 点击提交按钮提交最终的信息
# driver.find_element(By.CLASS_NAME, "button_search").click()


