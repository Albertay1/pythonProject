import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 访问浏览器
driver.get("https://console.bitasset.cc/#/login")
# 进入界面后等待10秒
driver.implicitly_wait(10)
# 输入谷歌验证码
driver.find_element('name', 'googleCode').send_keys("888888")
# 点击登录按钮进行登录
driver.find_element('xpath', '//*[@id="app"]/div/form/button').click()
# 点击列表展示
# driver.find_element("class", "hamburger")
# 登录完成后等待5秒钟再点击界面信息
# time.sleep(5)
# 点击交易参数管理
driver.find_element('xpath', '//*[@id="app"]/div/div[1]/div[1]/div/ul/div/li[1]/div').click()
# 点击币种参数管理
driver.find_element('xpath', '//*[@id="app"]/div/div[1]/div[1]/div/ul/div/li[1]/ul/a[1]/li').click()
# time.sleep(2)
# 选择需要查找的对象
driver.find_element_by_class_name('el-input__inner').click()
#
time.sleep(2)
# 选择手机号
driver.find_element('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()
# 在输入框输入手机号
driver.find_element('class', 'el-input__inner').send_keys('18267114517')
# 完成后等待5秒查看结果
time.sleep(5)
driver.quit()

