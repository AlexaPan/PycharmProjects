import scrapy


class LmparsSpider(scrapy.Spider):
    name = "lmpars"
    allowed_domains = ["lm-catalog.ru"]
    start_urls = ["https://lm-catalog.ru/product-category/osveshhenie/osveshhenie-zhilyh-pomeshhenij/torshery/"]

    def parse(self, response):
        pass
