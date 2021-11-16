from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys('TNT')
driver.find_element_by_xpath('//*[@id="nav_searchform"]/div/button').click()

handles = driver.window_handles
driver.switch_to.window(handles[1])

driver.find_element_by_xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a').click()

driver.switch_to.window(handles[2])
driver.find_element_by_xpath('//*[@class="van-icon-videodetails_like"]').click()
sleep(2)

driver.quit()

