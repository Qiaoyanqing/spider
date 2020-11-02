from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser = webdriver.Chrome()
browser.get(url)

browser.switch_to.frame("iframeResult")
try:
    log = browser.find_element_by_class_name("logo")
except NoSuchElementException:
    print("no logo")

browser.switch_to.parent_frame()# 切换到当前页面的父级页面

# 父级页面
logo = browser.find_element_by_class_name("logo")
print(logo)
print(logo.text)