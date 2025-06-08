import scrapy
from gaokao_scraper.items import GaokaoScraperItem
#抓取高考网图片
class GaokaoSpiderSpider(scrapy.Spider):
    name = "gaokao_spider"
    
    def start_requests(self):
        with open('urls.txt', 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        title = response.css("h1 > a::text").get()
        image_url = response.css('p[style*="text-align: center"] img::attr(src)').get()
        print(f'image_url :{image_url}')
        item = GaokaoScraperItem()
        item["title"] = title
        item["images"] = image_url
        item['image_urls'] = [response.urljoin(image_url)]  
        yield item
        
        # 处理分页：尝试获取下一页链接
        next_page = response.css('div.pages a:contains("下一页")::attr(href)').get()
        # 如果没有通过文本找到，尝试使用最后一个是下一页的情况
        if not next_page:
            next_page = response.css("div.pages > a:last-child::attr(href)").get()
        if next_page:
            print(f"Found next page: {next_page}")
            yield response.follow(next_page, callback=self.parse)
        else:
            print("No next page found.")