import scrapy
from Assignment.Assignment.items import ClothingItem


class SpiderFirstSpider(scrapy.Spider):
    name = "spider_first"
    allowed_domains = ["shop.mango.com"]
    start_urls = ["https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99", "https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07"]

    def parse(self, response):
        sizes = []
        clothing = ClothingItem()

        for size in response.css('ul.tGykN'):
            sizes.append(size.css('li button snap.text-title-m::text').gett())

        clothing['name'] = response.css('.product-name::text').get()
        clothing['price'] = response.css('snap.text-title-x1::text').get()
        clothing['color'] = response.css('div.color-container--selected').attrib['aria-label']
        clothing['size'] = sizes

        yield clothing

