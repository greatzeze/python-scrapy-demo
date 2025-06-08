# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import re


class GaokaoScraperPipeline:
    def process_item(self, item, spider):
        return item


class CustomImagesPipeline(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None, *, crawler=None):
        super().__init__(store_uri, download_func, settings, crawler=crawler)
        self.count = 0

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta["item"]
        # 清理标题中的非法文件名字符
        title = re.sub(r'[\\/*?:"<>|]', "", item["title"])
        return f"{title}.png"

    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            yield scrapy.Request(image_url, meta={"item": item})
