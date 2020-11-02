import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://baidu.com"
browser = webdriver.Chrome()# 构造一个web自动化工具
browser.get(url)# 打开目标网址
input = browser.find_element_by_id("kw")
input.send_keys("chromedriver配置")# 在定位处输入数据
input.send_keys(Keys.ENTER)# 执行键盘的回车
wait = WebDriverWait(browser,10)
wait.until(EC.presence_of_element_located((By.ID,"content_left")))
print(browser.current_url)
print(browser.get_cookies())

time.sleep(6)

browser.close()