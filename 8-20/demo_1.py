# import requests
#
# headers = {
#     "User-Agent":"Mozilla/2.0(Windows NT 10.0;Win64;x64"
# }
# url = "http://github.com/favicon.ico?name=qyq&args=123"
# data = {
#     'age':123444
# }
# response = requests.get(url = url , params = data)
# print(type(response))
# print(response.text)
# print(response.content)
#
# # with open("ababa.ico","wb") as f:
# #     f.write(response.content)

import requests

url = "http://www.zongheng.com/"

response = requests.get(url)

print("headers", type(response.headers),response.headers)
print("status",type(response.status_code),response.status_code)
print("URL",type(response.url),response.url)
print("history",type(response.history),response.history)
print("cookie",type(response.cookies),response.cookies)