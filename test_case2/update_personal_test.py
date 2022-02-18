import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "username").send_keys("ray1")
driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.CSS_SELECTOR, ".login_btn.fl").click()
driver.find_element(By.ID, "password").submit()
time.sleep(3)
# 2.1.点击”账号设置“
driver.find_element(By.LINK_TEXT, "账号设置").click()
# 2.2.点击“个人资料”
driver.find_element(By.PARTIAL_LINK_TEXT, "人资").click()
# 2.3.修改“真实姓名”
driver.find_element(By.ID, "true_name").clear()
driver.find_element(By.ID, "true_name").send_keys("曦")
# 2.4.选择“性别”
driver.find_element(By.CSS_SELECTOR, "[value = '1']").click()
# 2.5.输入“生日”
# 编写JavaScript代码删除一个内容，方便元素输入
script = 'document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(script)
driver.find_element(By.ID, "date").clear()
driver.find_element(By.ID, "date").send_keys("1995-10-04")
# 2.6.输入“QQ"
driver.find_element(By.ID, "qq").clear()
driver.find_element(By.ID, "qq").send_keys("175894")
# 2.7.点击“确认”
driver.find_element(By.CSS_SELECTOR, '[value = "确认"]').click()
# 显示等待
WebDriverWait(driver, 30, 0.5).until(expected_conditions.alert_is_present())
# time.sleep(3)
# 切换窗口至alert界面，点击确认按钮
update_status = driver.switch_to.alert.text
print(update_status)
driver.switch_to.alert.accept()
time.sleep(3)

