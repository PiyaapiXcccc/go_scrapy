import redis
import logging
from scrapy.exceptions import DropItem

class RedisPipeline(object):
    conn = None

    def open_spider(self, spider):
        self.conn = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def process_item(self, item, spider):
        if item['content'] == None:
            self.conn.sadd('un_success_content', item['id'])
            self.conn.hsetnx(name=item['id'], key='url', value=item['url'])
            self.conn.hsetnx(name=item['id'], key='img', value=item['img'])
            logging.warning("{} is void content".format(item['id']))
        else:
            try:
                self.conn.hsetnx(name=item['id'], key='url',value=item['url'])
                self.conn.hsetnx(name=item['id'], key='img',value=item['img'])
                self.conn.hsetnx(name=item['id'], key='content',value=item['content'])
            except Exception:
                self.conn.sadd('un_success_qipu', item['url'])
                logging.warning("Something is going wrong, Id:{}".format(item['id']))
                logging.warning("Content:{}".format(item['content']))
        return item

    def close_spider(self, spider):
        self.conn.close()

class DuplicatesPipeline(object):
    conn = None

    def __init__(self):
        self.conn = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def process_item(self, item, spider):
        if self.conn.sadd('success_qipu', item['id']) == 0:
            raise DropItem("这个棋谱已经被爬取了: %s" % item)
        else:
            return item

    def close_spider(self, spider):
        self.conn.close()
