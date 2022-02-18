# 打开浏览器
import time

from selenium import webdriver

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 设置隐式等待10秒
driver.implicitly_wait(10)
# 访问浏览器
driver.get("https://console.bitasset.cc/#/login")
# # 输入谷歌验证码
driver.find_element('name', 'googleCode').send_keys("888888")
# # 点击登录按钮进行登录
driver.find_element('xpath', '//*[@id="app"]/div/form/button').click()
# 设置显示等待3秒
time.sleep(3)
# 点击理财管理
driver.find_element('xpath', '//*[@id="app"]/div/div[1]/div[1]/div/ul/div/li[20]/div').click()
# 点击理财管理中都产品管理
driver.find_element('xpath', '//*[@id="app"]/div/div[1]/div[1]/div/ul/div/li[20]/ul/a[2]/li').click()
# 等待3秒
time.sleep(3)
# 点击添加按钮
driver.find_element('css_selector', '. el-button. el-button--primary. el-button--medium').click()
# 上传icon的图片
driver.find_element('name', 'file').send_keys("F:/LOGO/PNG/USDT.png")

