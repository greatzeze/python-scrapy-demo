# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GaokaoScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    image_urls = scrapy.Field()  # 用于传递给ImagesPipeline的图片URL列表
    images = scrapy.Field()      # 用于存储ImagesPipeline下载后的结果信息
    pass
