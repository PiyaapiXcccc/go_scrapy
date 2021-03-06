# Scrapy settings for go_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'go_scrapy'

SPIDER_MODULES = ['go_scrapy.spiders']
NEWSPIDER_MODULE = 'go_scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'utf-8'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

LOG_FILE = "test-15K.log"
LOG_LEVEL = "INFO"
LOG_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 'cookie':'csrftoken=kHaO7YPr3dOSflnczECPYWiIpj6LYopGwpQjGhvZRHKfhUPAaSuRPr754a1M2Uw9; sessionid=v5gimm0iq1a61h1o9vw5oeqblhvlg45i'
    'cookie':'csrftoken=NHNu6mwjVgm7Ix0Sp2UTV9xKAUmht0pdv4Jo6SdNIw2WMyXbaFgON4hDX5B7066I; sessionid=hf2oyjr5dqvugy7p40cdarzgw64ag2xr'
}
RETRY_TIMES = 5

HTTPERROR_ALLOWED_CODES = [302]
# HTTPERROR_ALLOWED_CODES = [302]
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'go_scrapy.middlewares.GoScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
         # 'go_scrapy.middlewares.ProxyMiddleWare':543,
        # 'scrapy.downloadermiddlewares.retry.RetryMiddleware':None
   }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'go_scrapy.RedisPipeline.RedisPipeline': 300,
   'go_scrapy.RedisPipeline.DuplicatesPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


######################################################
##############?????????Scrapy-Redis????????????################
######################################################

# ??????Redis?????????????????????
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
#
# # ???????????????Redis??????Requests??????
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # ?????????????????????????????????Redis??????????????????
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # ???Requests??????????????????Redis?????????????????????????????????
# SCHEDULER_PERSIST = True
#
# # Requests???????????????????????????????????????
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

