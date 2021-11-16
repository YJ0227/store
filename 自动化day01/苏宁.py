from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.suning.com")
driver.maximize_window()

# 定位搜索框并输入“小米”
driver.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys("小米")
# 点击搜索按钮
driver.find_element_by_xpath('//*[@id="searchSubmit"]').click()
sleep(2)

# 点击某个商品,查看详情
driver.find_element_by_xpath('//*[@id="0000000000-12333437343"]/div/div/div[2]/div[2]/a').click()
sleep(2)

# 切换第二个窗口
handles = driver.window_handles
driver.switch_to.window(handles[1])

# 添加购物车
driver.find_element_by_xpath('//*[@id="addCart"]').click()

sleep(2)
driver.quit()

