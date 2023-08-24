#https://www.youtube.com/watch?v=KmzvSo90Zj4
import scrapy

class GITSpider(scrapy.Spider):
    name = "GitHub"
    start_url = ["https://github.com/trending", ]

    def parse(self, response):
        for h2 in response.xpath('//h2'):
            yield {'h2_link': h2.xpath('.//a/@data-hydro-click-hmac').get()}




