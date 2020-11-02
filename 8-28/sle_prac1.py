# from selenium import webdriver
# url = "https://www.baidu.com/"
# browser = webdriver.Chrome()
# browser.get(url)
# point = browser.find_element_by_css_selector("#s-top-left")
# print(point)
# print(point.get_attribute("class"))
# import time
# time.sleep(2)
# browser.close()
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
browser.execute_script('alert("to Bottom")')
time.sleep(2)
browser.close()