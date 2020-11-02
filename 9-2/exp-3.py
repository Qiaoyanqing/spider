from urllib.parse import urljoin
from selenium import webdriver
import requests
import time

base_url = "http://login2.scrape.cuiqingcai.com/"
login_url = urljoin(base_url,"login")
index_url = urljoin(base_url,"index")

username = "admin"
password = "admin"

data = {
    "username":username,
    "password":password
}

browser = webdriver.Chrome()
browser.get(login_url)
browser.find_element_by_css_selector('input[name="username"]').send_keys(username)
browser.find_element_by_css_selector('input[name="password"]').send_keys(password)
browser.find_element_by_css_selector('input[type="submit"]').click()
time.sleep(2)
cookies = browser.get_cookies()
# for cookies in cookies:
#     print(cookies)
browser.close()

session = requests.Session()
for cookies in cookies:
    session.cookies.set(cookies["name"],cookies["value"])
res = session.get(index_url)
print(res.url)