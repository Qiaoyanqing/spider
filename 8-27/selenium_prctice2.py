from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
browser = webdriver.Chrome()
browser.get("http://www.taobao.com/")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#J_SiteNavLogin")
input_third = browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]')
print(input_first)
print(input_second)
print(input_third)
input_first.send_keys("phone")
input_first.clear()
input_first.send_keys("vivo")
time.sleep(2)
input_first.send_keys(Keys.ENTER)
input_first.send_keys("oppo")
input_first.clear()
input_first.send_keys("xiaomi")
input_first.send_keys(Keys.ENTER)



time.sleep(3)
browser.close()