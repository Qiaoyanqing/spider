import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'#爬虫的名字，全局唯一
    allowed_domains = ['quotes.toscrape.com']#允许爬取的域名
    start_urls = ['http://quotes.toscrape.com/']#spider启动时爬取的列表，初始请求由它定义

    def parse(self, response):
        #spider的一个方法，默认情况下被调用的start_url里的连接构成的请求完成下载后，返回的响应就会传递给这个函数，然后进行解析，提取数据或者进行下一步的爬取
        pass
