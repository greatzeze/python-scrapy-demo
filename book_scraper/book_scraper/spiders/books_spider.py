import scrapy
from book_scraper.items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/index.html"]

    def parse(self, response):
        # 解析书籍列表
        for book in response.css('article.product_pod'):
            item = BookItem()
            
            item["title"] = book.css("h3 a::attr(title)").get()
            item["price"] = book.css("p.price_color::text").get()
            item["stock_status"] = book.css("p.instock::text")[1].get().strip()
            
            # 处理星级评分
            rating_class = book.css("p.star-rating::attr(class)").get()
            item["rating"] = rating_class.split()[-1]
            
            yield item

        # 处理分页
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)