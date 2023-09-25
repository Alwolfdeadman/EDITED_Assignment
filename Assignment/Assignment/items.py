# Define here the models for your scraped items
import scrapy


class ClothingItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
