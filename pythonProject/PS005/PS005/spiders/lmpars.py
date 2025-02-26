import scrapy


class LmparsSpider(scrapy.Spider):
    name = "lmpars"
    allowed_domains = ["lm-catalog.ru"]
    start_urls = ["https://lm-catalog.ru/product-category/osveshhenie/osveshhenie-zhilyh-pomeshhenij/torshery/"]

    def parse(self, response):
        torshers = response.css('div.shop-item-inner')
        for torsher in torshers:
            yield {
                'name': torsher.css('div.shop-item__title a::text').get(),
                'price': torsher.css('div.shop-item__price bdi::text').get(),
                'link': torsher.css('div.shop-item__title a::attr(href)').get()
            }

        # Опционально: обработка пагинации
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)