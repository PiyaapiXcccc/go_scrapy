import scrapy
import logging


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['search.smzdm.com']
    start_urls = ['https://search.smzdm.com/?c=home&s=%E7%89%9B%E5%A5%B6&v=b&p=1']

    def parse(self, response):
        logging.info(response.css('title'))

        next = response.xpath('//*[@id="J_feed_pagenation"]/li[last()]/a/@href').get()
        logging.info(next)
        yield response.follow(next, callback=self.parse)
