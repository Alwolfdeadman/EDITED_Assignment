import scrapy


class SpiderFirstSpider(scrapy.Spider):
    name = "spider_first"
    allowed_domains = ["shop.mango.com"]
    start_urls = ["https://shop.mango.com"]

    def parse(self, response):
        pass
