# import requests
#
# url = "http://www.baidu.com"
#
# response = requests.get(url = url)
#
# if response.status_code is requests.codes.ok:#判断请求否成功
#     print(response.cookies)
#     for key , value in response.cookies.items():
#         print(f"{key} = {value}")
#         print("{} = {}".format(key,value))
#
# import requests
#
# url = "http://httpbin.org/cookies/set/key/value"#set是一个方法，后面可以随便写
#
# requests.get(url=url)#设置cookis
#
# #自己请求我们的cookies
#
# response = requests.get(url="http://httpbin.org/cookies")
#
# print(response.text)
#
# my_session = requests.Session()
# my_session.get((url))# 利用session先在服务端设置了一个cookies
#
# # response_2 = my_session.get(url="http://httpbin.org/cookies")
# # print(response_2.text)
# import requests
#
# headers = {
#     "header":"cookise_value",
#     "User-Agent":"Mozilla/2.0(Windows NT 10.0;Win64;x64)"
# }
# response = requests.get(url="http://github.com/",headers=headers,timeout = 1)
# if response.status_code is requests.codes.ok:
#     print(response.text)
# import requests
# from requests.auth import HTTPBasicAuth
# url = "http://httpbin.org/basic-auth/qyq/123"
#
# response = requests.get(url,auth = HTTPBasicAuth("qyq","123"))
# print(response.status_code)
# print(response.text)
#
# response_2 = requests.get(url,auth = HTTPBasicAuth("qyq","123"))
# print(response_2.status_code)
# print(response_2.text)
# import requests
# proxies = {
#     "https":"https://221.229.252.98:9797",
#     "http":"http://221.229.252.98:9797"
# }
# url = "http://httpbin.org/get"
# response = requests.get(url,proxies = proxies)
# print(response.status_code)
# print(response.text)
import re

str = 'hello world 1234 qyq'

content = re.match("^hello\s\w{5}\s\d{4}\s\w{3}$",str)
print(type(content.group()))
print(content.group())