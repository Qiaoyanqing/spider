from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame("iframeResult")
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
import time
time.sleep(3)
browser.close()


# from selenium import webdriver
#
# browser = webdriver.Chrome()
# url = "http://www.zongheng.com/"
#
# browser.get(url)
# # 定位
# point = browser.find_element_by_css_selector('[title = "奇幻玄幻"]')
# # 文本获取
# print(point.text)
# # 获取ID、位置、标签名、大小
# # id属性可以获取节点的id，location属性可以获取节点在
# print("id",point.id)
# print("location",point.location)
# print("size",point.size)
# print("tag_name:",point.tag_name)

# browser.close()