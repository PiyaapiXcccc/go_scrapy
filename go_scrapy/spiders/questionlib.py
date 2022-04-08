import scrapy
import logging
import time
from go_scrapy.items import QipuItem

class QuestionlibSpider(scrapy.Spider):
    name = 'questionlib'
    allowed_domains = ['www.101weiqi.com']
    start_urls = ['http://www.101weiqi.com/questionlib/']
    path = "./级位题目分类/"


    def parse(self, response):
        diff_type = response.xpath('//*[@id="main"]/div[2]/div[1]/div[4]/div/a/text()').getall()
        diff_type_url = response.xpath('//*[@id="main"]/div[2]/div[1]/div[4]/div/a/@href').getall()
        logging.info(diff_type)
        for (index, page) in enumerate(diff_type_url):
            yield response.follow(page, callback=self.parse_type)

    def parse_type(self, response):
        qipu_urls = response.xpath('//*[@id="main"]/div[2]/div/div[1]/div/a/@href').getall()
        imgs = response.xpath('//*[@id="main"]/div[2]/div/div[1]/div/a/img/@src').getall()
        next = response.xpath('//*[@id="main"]/div[2]/div/div[3]/ul/li[last()]/a/@href').get()

        for (index, url) in enumerate(qipu_urls):
            # logging.info("11111 url:{}".format(url))
            # logging.info("11111 img_url:{}".format(imgs[index]))
            yield response.follow(url, callback=self.parse_detail_qipu, meta={'qipuid':url, 'img_url':imgs[index],'dont_redirect': True, 'handle_httpstatus_list': [302]})
            # yield response.follow(url, callback=self.parse_detail_qipu)
        if next != '#':
            yield response.follow(next, callback=self.parse_type)


    def parse_detail_qipu(self, response):
        content = response.xpath('//script[starts-with(text(), "var static_server")]').get()
        logging.info("id:{}".format(response.meta['qipuid']))
        logging.info("url:{}".format(response.url))
        logging.info("img:{}".format(response.meta['img_url']))
        if content == None:
            logging.info("response :{}".format(response))
            logging.info("response text :{}".format(response.text))
            logging.info("账号被ban，暂停1分钟.........")
            time.sleep(1 * 60)
        item = QipuItem()
        item['id'] = response.meta['qipuid']
        item['url'] = response.url
        item['img'] = response.meta['img_url']
        item['content'] = content

        return item