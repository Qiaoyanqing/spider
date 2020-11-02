from pyquery import PyQuery
# import pymongo
#
# client = pymongo.MongoClient("mongodb://localhost:27017")
# db = client["spider_practice"]
# collection = db["spider_books"]
# collection.remove()
# # 创建链接对象
#
# client = pymongo.MongoClient(host="127.0.0.1",port=27017)# host = "localhost" port端口号
#
# # 指定链接数据库
# db = client["spider_practice"]# 链接到数据库spider_practice
# collection = db["teachers"]# 链接到数据库下的students表
#
# headers = {
#     "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# }
#
# # total_page = 2
# start_url = "http://www.zongheng.com/rank/details.html?rt=1&d=1&i=2"
#
# doc = PyQuery(url=start_url)
#
# name_list = []
# auther_list = []
# type_list = []
# clicmember_list = []
# img_url_list = []
# text = {}
# for i in doc(".rank_d_b_name").items():
#     name = i.attr("title")
#     name_list.append(name)
#
# for i in doc(".rank_d_b_cate a").eq(1).items():
#     print(i.text())
#     py = i.text()
#     type_list.append(py)
#
# for i in doc(".rank_d_b_cate").items():
#     au_name = i.attr("title")
#     auther_list.append(au_name)
#
# for i in doc(".rank_d_book_img.fl a").items():
#     hrefs = i.attr("src")
#     img_url_list.append(hrefs)
#
# for i in doc(".rank_d_b_ticket").items():
#     clicmember_list.append(i)
# for i in range(len(type_list)):
#     text = {
#         'bookname': name_list[i],
#         'auther': auther_list[i],
#         'type': type_list[i],
#         'clicmember': clicmember_list[i],
#         'img_url': img_url_list[i]
#     }
#     print(text)
#     # res = collection.insert_one(text)
#
#
# # links = []
# #
# # for i in doc(".rank_d_book_img.fl a").items():
# #     href = i.attr("href")
# #     links.append(href)
# #
# #
# # for i in range(len(links)):
# #     hrefs = {
# #         'href':links[i]
# #     }
# #     result = collection.insert_one(hrefs)
import asyncio
import time
import requests
import aiohttp

start_time = time.time()

async def get(url):
    session = aiohttp.ClientSession()#  构建aiohttp的client
    response = await session.get(url)
    await response.text()
    # await response.status()
    await session.close()
    return requests.get(url)

def request():
    url = "http://books.toscrape.com/catalogue/page-2.html"
    print(f"waiting for {url}")
    response = await get(url)
    print(f"get response for {url}")
tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print("cost time:",end_time-start_time)