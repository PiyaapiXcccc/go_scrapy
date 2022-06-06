import scrapy
import redis
import logging
import time
from go_scrapy.items import QipuItem

class OneKSpider(scrapy.Spider):
    name = 'one_K'
    allowed_domains = ['www.101weiqi.com']
    step = 9
    start_urls = ['https://www.101weiqi.com/{}K/'.format(step)]

    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    step_qipu_set =  set(r.keys("/{}K*".format(step)))


    def parse(self, response):

        qipu_urls = response.xpath('//*[@id="main"]/div[2]/div/div[1]/div/a/@href').getall()
        imgs = response.xpath('//*[@id="main"]/div[2]/div/div[1]/div/a/img/@src').getall()
        next = response.xpath('//*[@id="main"]/div[2]/div/div[3]/ul/li[last()]/a/@href').get()
        # 去重
        new_qipu_urls = list(set(qipu_urls).difference(self.step_qipu_set))

        for (index, url) in enumerate(new_qipu_urls):
            yield response.follow(url, callback=self.parse_detail_qipu,
                                  meta={'qipuid': url, 'img_url': imgs[index], 'dont_redirect': True,
                                        'handle_httpstatus_list': [302]})
            # yield response.follow(url, callback=self.parse_detail_qipu)
        if next != '#':
            yield response.follow(next, callback=self.parse)

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