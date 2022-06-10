# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
import requests

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class GoScrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GoScrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleWare(object):

    def process_request(self, request, spider):
        """ 对 request 加上proxy"""
        # proxies = ["39.107.227.240:3128", "81.68.243.42:80", "111.229.237.116:3128"
        #            ,"222.69.240.130:8001","120.42.46.226:6666","218.1.142.142:57114"
        #         ,"61.164.39.68:53281"]
        # old_proxy = request.meta.get('proxy')
        # print('---------this is old_proxy ip ----------:{}'.format(old_proxy))
        # if old_proxy == None:
        #     proxy = requests.get("http://127.0.0.1:5010/get?type=https").json().get("proxy")
        #     # proxy = random.sample(proxies, 1)[0]
        #     print('---------this is request ip ----------:{}'.format(proxy))
        #     request.meta['proxy'] = 'https://' + proxy

        proxy = requests.get("http://127.0.0.1:5010/get").json().get("proxy")
        is_https = requests.get("http://127.0.0.1:5010/get").json().get("https")
        if is_https == False :
            str = "http://"
        else:
            str = "https://"

        print('---------this is request ip ----------:{}'.format(proxy))
        request.meta['proxy'] = str + proxy



    def process_response(self, request, response, spider):
        """ 对返回的 response 处理"""

        # 如果返回的 response 状态不是 200， 重新生成当前的 request对象
        if response.status != 200:
            origin_proxy = request.meta['proxy']
            requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(origin_proxy))
            proxy = requests.get("http://127.0.0.1:5010/get?type=https").json().get("proxy")
            request.meta['proxy'] = 'https://' + proxy
            print('200 this is new response ip:' + proxy)
            # 对当前 request 加上代理
            return request

        return response

    def process_exception(self, request, exception, spider):
        # self.logger.debug('Try Exception time')
        # self.logger.debug('Try second time')
        proxy_addr = requests.get("http://127.0.0.1:5010/get/").json().get("proxy")
        is_https = requests.get("http://127.0.0.1:5010/get/").json().get("https")
        if is_https == False :
            request.meta['proxy'] = 'http://' + proxy_addr
        else:
            request.meta['proxy'] = 'https://' + proxy_addr
        return request