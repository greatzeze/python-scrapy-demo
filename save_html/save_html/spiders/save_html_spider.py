import scrapy
import os


class SaveHtmlSpiderSpider(scrapy.Spider):
    name = "save_html_spider"
    allowed_domains = ["https://www.baidu.com/"]
    start_urls = ["https://www.baidu.com/"]

    def parse(self, response):
        filename = "baidu.html"
        filapath = os.path.join("saved_pages", filename)
        with open(filapath, "wb") as f:
            f.write(response.body)
        self.log(f"保存文件：{filapath}")
        pass
