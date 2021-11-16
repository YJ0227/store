from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.jd.com")
driver.maximize_window()

# 定位搜索框并输入“thinkpad  e580”
driver.find_element_by_xpath("//*[@id='key']").send_keys("thinkpad  e580")
# 点击搜索按钮
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

# 点击某个商品,查看详情
driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[2]/div/div[3]/a').click()
sleep(2)

# 切换第二个窗口
data = driver.window_handles
driver.switch_to.window(data[1])

# 添加购物车
driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()

sleep(2)
driver.quit()





