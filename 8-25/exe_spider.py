import time
import pymongo
import requests
from pyquery import PyQuery
import logging# 日志


logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s - %(levelname)s:%(message)s"
)

# 构建一个头信息，避免被网站识别为机器人
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

total_page = 2
start_url = "http://www.zongheng.com/rank/details.html?rt=1&d=1&i=2&p={}"

def scrape_page(url):
    '''
    获取页面的html文本
    :param url:
    :return:
    '''

    logging.info("scraping %s..",url)
    try:
        response = requests.get(url,headers= headers)
        if response.status_code is requests.codes.ok:
            # print(response.text)
            return response.text
        logging.error("get %S is not 200", url)
        return None
    except requests.RequestException as e:
        logging.error("scraping error %s",e)

def scrape_index(page):
    '''
    构造url
    返回url的页面文本
    :param page:
    :return:
    '''

    index_url = start_url.format(page)
    # print(index_url)
    return scrape_page(index_url)

def parse_index(html):
    '''
    解析获取每个书籍详情的url
    :param html: 指一级页面文本
    :return:
    '''
    doc = PyQuery(html)
    # divs 根据标签获取class - rank。。。。的代码块返回子节点
    divs = doc(".rankpage_box").children(".rank_d_list")
    # 循环拿出子节点内容
    for div in divs.items():
        # 根据class属性定位a标签
        a = div(".rank_d_book_img a")
        # 获取href属性值
        href = a.attr("href")
        yield href  # 通过迭代 挨个返回上一级

    # links = []
    # for a in doc(".rank_d_book_img.fl a").items():
    #     href = a.attr("href")
    #     links.append(href)
    # return links

def scrape_detail(url):
    '''
    获取详情页面的文本信息
    :param url:
    :return:
    '''

    return scrape_page(url)

def parse_detail(html):
    '''
    解析页面信息
    :param html:
    :return:
    '''

    doc = PyQuery(html)
    book_side = doc(".book-top").children(".book-side")
    book_info = doc(".book-top .book-main .book-detail .book-info")

    book_name = book_info.children(".book-name").text()
    type = book_info.children(".book-label .label").text()
    statu = book_info.children(".book-label .state").text()
    numbers = book_info.children(".nums") # 将四个span都取出来
    # num("i")取出span中的i标签
    clicknumbers = [num("i").text() for num in numbers.items()][0].split(" ")[2] # 一共有4个span，取第三个（及2）for循环遍历

    intro = book_info.children(".book-dec").text()#简介
    img_url = book_info.siblings(".book-img img").attr("src")
    author = book_side.children(".book-author .au-name a").text()

    return {
        'bookname':book_name,
        'author':author,
        'type':type,
        'status':statu,
        'intro':intro,
        'clickmember':clicknumbers,
        'img_url':img_url
    }

def save(data):
    # 根据bookname在数据库中进行查询，如果说bookname已经存在,就更新这个bookname中的数据，否则就插入一条新的数据
    # 这是update_one中upsert=True的作用
    collection.update_one(
        {
        'bookname':data.get("book_name"),
        'author':data.get("author"),
        'type':data.get("type"),
        'status':data.get("statu"),
        'intro':data.get("intro"),
        'clickmember':data.get("clicknumbers"),
        'img_url':data.get("img_url")
        },
        {"$set":data},
        upsert = True
    )

def img_save(data):

    url = data["img_url"]
    img_name = data["bookname"]

    image = requests.get(url,headers=headers)

    if image.status_code is not requests.codes.ok:
        return None
    with open(f"./image/{img_name}.jpeg","wb") as f:
        f.write(image.content)

if __name__ == '__main__':
    # 数据库的链接
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["books"]
    collection = db["books"]

    for i in range(1,total_page):
        html = scrape_index(i)
        if html is None:
            logging.info(f"{i} page is error")
            exit()
        # print('*'*30)
        # print(html)
        urls = parse_index(html)
        # print(parse_index(html))
        for url in urls:
            detail_html = scrape_detail(url)
            if detail_html is None:
                logging.info("url requests is error")
                continue
            detail_info = parse_detail(detail_html)
            # print(detail_info)
            save(detail_info)
            img_save(detail_info)
            time.sleep(5)

#
# html = requests.get(url=start_url.format(1),headers=headers)
#
# if html.status_code is not requests.codes.ok:
#     print("requests error")
#     exit()
# print(html.text)


