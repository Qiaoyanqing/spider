import requests
from urllib.parse import urljoin

base_url = "http://login2.scrape.cuiqingcai.com/"
login_url = urljoin(base_url,"login")
index_url = urljoin(base_url,"index")

username = "admin"
password = "admin"

data = {
    "username":username,
    "password":password
}
session = requests.Session()
response_login = session.post(login_url,data=data)
cookies = session.cookies
print(cookies)
response_index = session.get(index_url)
print(response_index.url)
response = requests.post(url=login_url,data=data,allow_redirect=False)# 不让该浏览器做重定向allow_redirect=False（默认为TRUE）
