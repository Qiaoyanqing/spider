import time
from urllib.parse import urljoin

import pymongo
import requests
from pyquery import PyQuery


headers = {
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

start_url ="http://books.toscrape.com/catalogue/page-{}.html"


def scrape_page(url):
    response = requests.get(url,headers=headers)
    if response.status_code is  requests.codes.ok:
        return response.text

def scrape_index(page):
    index_url = start_url.format(page)
    return scrape_page(index_url)

def parse_url(html):
    doc = PyQuery(html)
    divs = doc(".col-xs-6").children(".product_pod")
    for a in divs(".image_container a").items():
        href = a.attr("href")
        url = urljoin("http://books.toscrape.com/catalogue/",href)
        yield url

def scrape_detail(url):
    return scrape_page(url)

def parse_detail(html):
    doc = PyQuery(html)
    product_main = doc(".col-sm-6.product_main")
    book_name = product_main.children("h1").text()
    book_price = product_main.children(".price_color").text()
    des = doc(".product_page p").text()

    # tbody = doc(".table table-striped tbody").children()
    # UPC = [num("td").text() for num in tbody.items()][0].split()[0]
    # tax = [num("td").text() for num in tbody.items()][0].split()[4]
    # availability = [num("td").text() for num in tbody.items()][0].split([5])
    img_url = urljoin("http://books.toscrape.com",doc(".row .col-sm-6 #product_gallery .item img").attr("src"))
    return {
        "Bookname":book_name,
        # "UPC":UPC,
        "Description":des,
        "Price":book_price,
        # "tax":tax,
        # "availability":availability,
        "img_url":img_url
    }
def img_save(data):
    url = data["img_url"]
    img_name = data["Bookname"]

    image = requests.get(url,headers=headers)

    with open(f"./image/{img_name}.jpg","wb") as f:
        f.write(image.content)

def save(data):
    collection.update_one({
        "Bookname": data.get("Bookname"),
        # "UPC": data.get("UDP"),
        # "Description": data.get("des"),
        # "Price": data.get("bookprice"),
        # "Tax": data.get("tax"),
        # "Availability": data.get("availability"),
    },
    {"$set":data},
    upsert=True
    )
if __name__ == '__main__':

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["spider_practice"]
    collection = db["spider_books"]

    for i in range(1,2):
        html = scrape_index(i)
        urls = parse_url(html)

        for url in urls:
            # new_url = urljoin("http://books.toscrape.com/catalogue/",url)
            # print(url)
            detail_html = scrape_detail(url)
            detail_info = parse_detail(detail_html)
            save(detail_info)
            img_save(detail_info)
            time.sleep(1)