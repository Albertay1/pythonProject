import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://129.211.129.101:9007/index.php?m=user&c=public&a=login")
driver.find_element(By.ID, "username").send_keys("ray1")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".login_btn.fl").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "进入商城购物").click()
driver.find_element(By.NAME, "keyword").send_keys("iphone")
driver.find_element(By.CLASS_NAME, "btn1").click()
# driver.find_element(By.CLASS_NAME, "").click()
driver.find_elements(By.CLASS_NAME, "shop_01-imgbox")[1].click()
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
driver.find_element(By.ID, "joinCarButton").click()
driver.find_element(By.CLASS_NAME, "shopCar_T_span3").click()
driver.find_element(By.CSS_SELECTOR, ".shopCar_btn_03.fl").click()
driver.find_element(By.CLASS_NAME, "add-address").click()
driver.find_element(By.NAME, "address[address_name]").send_keys("ray")
driver.find_element(By.NAME, "address[mobile]").send_keys("1822222222")
sheng = driver.find_element(By.ID, "add-new-area-select")
Select(sheng).select_by_visible_text("山西省")
shi = driver.find_elements(By.CLASS_NAME, "add-new-area-select")[1]
Select(shi).select_by_visible_text("太原市")
qu = driver.find_elements(By.TAG_NAME, "select")[2]
Select(qu).select_by_visible_text("市辖区")

# time.sleep(3)
# driver.close()
