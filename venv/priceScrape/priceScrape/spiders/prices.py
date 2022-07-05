import base64
import json
import scrapy
from scrapy_splash import SplashRequest


class PricesSpider(scrapy.Spider):
    name = "prices"

    start_urls = "https://www.woolworths.com.au/shop/browse/meat-seafood-deli/meat/beef-veal"

    def start_requests(self):
        yield SplashRequest(self.start_urls, self.parse, args={'wait': 1.5})

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
