# -*- coding: utf-8 -*-

# Scrapy settings for www_zhipin_com_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'www_zhipin_com_test'

SPIDER_MODULES = ['www_zhipin_com_test.spiders']
NEWSPIDER_MODULE = 'www_zhipin_com_test.spiders'
FEED_EXPORT_ENCODING = 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'www_zhipin_com_test (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'www_zhipin_com_test.middlewares.WwwZhipinComTestSpiderMiddleware': 543,
# }

DOWNLOADER_MIDDLEWARES = {
   # 'www_zhipin_com.middlewares.WwwZhipinComDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
    'www_zhipin_com_test.middlewares.MyproxiesSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'www_zhipin_com_test.middlewares.WwwZhipinComTestDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'www_zhipin_com_test.pipelines.WwwZhipinComTestPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
IPPOOL = [{'ip_port': '111.201.27.78:9000', 'user_pass': ''},
          {'ip_port': '183.30.204.132:9999', 'user_pass': ''},
          {'ip_port': '27.46.20.104:888', 'user_pass': ''},
          {'ip_port': '27.46.20.129:888', 'user_pass': ''},
          {'ip_port': '119.122.3.26:9000', 'user_pass': ''},
          {'ip_port': '219.137.73.160:53281', 'user_pass': ''},
          {'ip_port': '113.87.162.13:8088', 'user_pass': ''},
          {'ip_port': '110.52.8.155:53281', 'user_pass': ''},
          {'ip_port': '113.88.209.50:9797', 'user_pass': ''},
          {'ip_port': '27.46.20.116:888', 'user_pass': ''},
          {'ip_port': '106.113.243.168:9999', 'user_pass': ''},
          {'ip_port': '119.123.177.60:9000', 'user_pass': ''},
          {'ip_port': '27.44.198.95:9999', 'user_pass': ''},
          {'ip_port': '27.44.168.208:9797', 'user_pass': ''},
          {'ip_port': '116.226.217.141:9999', 'user_pass': ''},
          {'ip_port': '182.121.200.21:9999', 'user_pass': ''},
          {'ip_port': '14.155.115.173:9000', 'user_pass': ''},
          {'ip_port': '27.44.196.43:9999', 'user_pass': ''},
          {'ip_port': '14.221.165.196:9797', 'user_pass': ''},
          {'ip_port': '115.229.28.227:9000', 'user_pass': ''},
          {'ip_port': '183.14.25.110:9000', 'user_pass': ''},
          {'ip_port': '111.230.244.98:3128', 'user_pass': ''},
          {'ip_port': '49.72.213.181:3128', 'user_pass': ''},
          {'ip_port': '112.95.22.66:8888', 'user_pass': ''},
          {'ip_port': '112.95.22.62:8888', 'user_pass': ''},
          {'ip_port': '115.233.210.218:808', 'user_pass': ''},
          {'ip_port': '220.178.145.146:45619', 'user_pass': ''},
          {'ip_port': '220.166.14.94:9797', 'user_pass': ''},
          {'ip_port': '182.88.12.225:9797', 'user_pass': ''},
          {'ip_port': '123.5.156.208:9000', 'user_pass': ''},
          {'ip_port': '114.249.116.158:9000', 'user_pass': ''},
          {'ip_port': '14.153.53.0:3128', 'user_pass': ''},
          {'ip_port': '27.44.175.169:9797', 'user_pass': ''},
          {'ip_port': '125.118.73.95:3128', 'user_pass': ''},
          {'ip_port': '183.30.204.131:9999', 'user_pass': ''},
          {'ip_port': '119.122.214.237:9000', 'user_pass': ''},
          {'ip_port': '27.44.198.63:9999', 'user_pass': ''},
          {'ip_port': '27.42.148.8:9797', 'user_pass': ''},
          {'ip_port': '113.88.208.201:9797', 'user_pass': ''},
          {'ip_port': '218.20.54.59:9999', 'user_pass': ''},
          {'ip_port': '113.65.127.237:9999', 'user_pass': ''},
          {'ip_port': '183.30.201.116:9797', 'user_pass': ''},
          {'ip_port': '125.89.53.239:9797', 'user_pass': ''},
          {'ip_port': '112.67.184.207:9797', 'user_pass': ''},
          {'ip_port': '218.20.55.33:9797', 'user_pass': ''},
          {'ip_port': '218.20.55.11:9999', 'user_pass': ''},
          {'ip_port': '218.20.54.38:9999', 'user_pass': ''},
          {'ip_port': '27.44.197.192:9999', 'user_pass': ''},
          {'ip_port': '221.223.140.69:9000', 'user_pass': ''},
          {'ip_port': '218.19.244.29:9000', 'user_pass': ''},
          {'ip_port': '119.123.178.83:9000', 'user_pass': ''},
          {'ip_port': '113.76.96.45:9797', 'user_pass': ''},
          {'ip_port': '113.118.96.111:9797', 'user_pass': ''},
          {'ip_port': '14.153.55.169:3128', 'user_pass': ''},
          {'ip_port': '218.20.55.57:9797', 'user_pass': ''},
          {'ip_port': '27.44.196.217:9999', 'user_pass': ''},
          {'ip_port': '119.136.198.141:9797', 'user_pass': ''},
          {'ip_port': '113.88.190.161:9797', 'user_pass': ''},
          {'ip_port': '163.125.16.10:8888', 'user_pass': ''},
          {'ip_port': '218.20.55.125:9999', 'user_pass': ''},
          {'ip_port': '27.46.32.219:9797', 'user_pass': ''},
          {'ip_port': '218.89.148.128:9999', 'user_pass': ''},
          {'ip_port': '106.42.65.221:9000', 'user_pass': ''},
          {'ip_port': '171.37.176.115:9797', 'user_pass': ''},
          {'ip_port': '171.37.28.35:9797', 'user_pass': ''},
          {'ip_port': '101.81.110.213:9000', 'user_pass': ''},
          {'ip_port': '112.95.90.133:9797', 'user_pass': ''},
          {'ip_port': '14.153.55.228:3128', 'user_pass': ''},
          {'ip_port': '42.233.104.253:9999', 'user_pass': ''},
          {'ip_port': '113.88.65.144:9797', 'user_pass': ''},
          {'ip_port': '113.78.64.133:9797', 'user_pass': ''},
          {'ip_port': '183.30.201.219:9797', 'user_pass': ''},
          {'ip_port': '182.88.116.234:9797', 'user_pass': ''},
          {'ip_port': '61.144.105.3:9797', 'user_pass': ''},
          {'ip_port': '182.88.165.243:9797', 'user_pass': ''},
          {'ip_port': '27.44.199.172:9999', 'user_pass': ''},
          {'ip_port': '218.19.244.171:9000', 'user_pass': ''},
          {'ip_port': '110.80.152.31:8118', 'user_pass': ''},
          {'ip_port': '116.17.127.228:9999', 'user_pass': ''},
          {'ip_port': '175.171.189.101:53281', 'user_pass': ''},
          {'ip_port': '218.20.55.22:9797', 'user_pass': ''},
          {'ip_port': '59.39.129.254:9000', 'user_pass': ''},
          {'ip_port': '218.20.55.187:9797', 'user_pass': ''},
          {'ip_port': '113.88.211.242:9797', 'user_pass': ''},
          {'ip_port': '120.84.229.119:9000', 'user_pass': ''},
          {'ip_port': '218.20.54.115:9797', 'user_pass': ''},
          {'ip_port': '113.87.162.140:808', 'user_pass': ''},
          {'ip_port': '218.20.55.105:9999', 'user_pass': ''},
          {'ip_port': '218.20.54.2:9797', 'user_pass': ''},
          {'ip_port': '113.89.52.97:9999', 'user_pass': ''},
          {'ip_port': '218.20.54.64:9797', 'user_pass': ''},
          {'ip_port': '175.171.181.48:53281', 'user_pass': ''},
          {'ip_port': '163.125.157.111:8888', 'user_pass': ''},
          {'ip_port': '27.44.197.20:9797', 'user_pass': ''},
          {'ip_port': '27.46.22.22:888', 'user_pass': ''},
          {'ip_port': '171.116.60.154:9797', 'user_pass': ''},
          {'ip_port': '123.14.226.4:8080', 'user_pass': ''},
          {'ip_port': '182.88.8.173:9797', 'user_pass': ''},
          {'ip_port': '183.134.59.138:80', 'user_pass': ''},
          {'ip_port': '112.250.65.222:53281', 'user_pass': ''},
          {'ip_port': '110.209.250.202:8118', 'user_pass': ''},
          {'ip_port': 'http:122.114.31.177:808', 'user_pass': ''},
          {'ip_port': '182.88.10.12:8118', 'user_pass': ''},
          {'ip_port': '1.194.128.235:31298', 'user_pass': ''},
          {'ip_port': '180.119.65.120:3128', 'user_pass': ''},
          {'ip_port': '140.250.138.183:28678', 'user_pass': ''},
          {'ip_port': 'http:118.114.77.47:8080', 'user_pass': ''},
          {'ip_port': '115.213.206.93:26871', 'user_pass': ''},
          {'ip_port': '60.167.22.158:33506', 'user_pass': ''},
          {'ip_port': '42.177.128.72:43029', 'user_pass': ''},
          {'ip_port': '113.79.75.73:808', 'user_pass': ''},
          {'ip_port': 'http:112.228.159.80:8118', 'user_pass': ''},
          {'ip_port': '115.213.200.213:808', 'user_pass': ''},
          {'ip_port': '180.120.209.178:3128', 'user_pass': ''},
          {'ip_port': '121.207.0.42:808', 'user_pass': ''},
          {'ip_port': '117.83.106.23:8118', 'user_pass': ''},
          {'ip_port': '122.241.223.112:37296', 'user_pass': ''},
          {'ip_port': '118.254.155.202:3128', 'user_pass': ''},
          {'ip_port': '171.8.168.58:48770', 'user_pass': ''},
          {'ip_port': '1.199.194.162:47319', 'user_pass': ''},
          {'ip_port': '36.49.82.187:80', 'user_pass': ''},
          {'ip_port': '27.153.128.108:41935', 'user_pass': ''},
          {'ip_port': '59.32.37.209:3128', 'user_pass': ''},
          {'ip_port': '180.118.243.109:808', 'user_pass': ''},
          {'ip_port': '120.38.103.88:27102', 'user_pass': ''},
          {'ip_port': '106.42.88.64:30046', 'user_pass': ''},
          {'ip_port': '116.231.60.140:8118', 'user_pass': ''},
          {'ip_port': '115.213.254.213:33710', 'user_pass': ''},
          {'ip_port': '113.105.203.58:3128', 'user_pass': ''},
          {'ip_port': '123.118.25.141:8118', 'user_pass': ''},
          {'ip_port': '121.226.168.124:43820', 'user_pass': ''},
          {'ip_port': '27.40.151.120:61234', 'user_pass': ''},
          {'ip_port': '182.39.8.151:48545', 'user_pass': ''},
          {'ip_port': '183.149.235.195:40525', 'user_pass': ''},
          {'ip_port': '114.238.147.216:24169', 'user_pass': ''},
          {'ip_port': '115.237.237.247:3128', 'user_pass': ''},
          {'ip_port': '112.254.181.4:8118', 'user_pass': ''},
          {'ip_port': '115.213.233.218:49468', 'user_pass': ''},
          {'ip_port': '114.218.139.138:38260', 'user_pass': ''},
          {'ip_port': '114.232.106.225:47790', 'user_pass': ''},
          {'ip_port': '110.88.112.238:20561', 'user_pass': ''},
          {'ip_port': '59.58.240.62:27881', 'user_pass': ''},
          {'ip_port': '222.79.248.165:49901', 'user_pass': ''},
          {'ip_port': '220.162.150.33:8888', 'user_pass': ''},
          {'ip_port': '118.254.152.55:3128', 'user_pass': ''},
          {'ip_port': '182.42.244.205:808', 'user_pass': ''},
          {'ip_port': '42.87.146.140:80', 'user_pass': ''},
          {'ip_port': '171.38.64.191:8123', 'user_pass': ''},
          {'ip_port': '115.46.78.189:8123', 'user_pass': ''},
          {'ip_port': '171.39.2.175:8123', 'user_pass': ''},
          {'ip_port': '123.149.160.227:22635', 'user_pass': ''},
          {'ip_port': '123.169.4.50:30097', 'user_pass': ''},
          {'ip_port': '110.72.26.252:8123', 'user_pass': ''},
          {'ip_port': '115.46.89.254:8123', 'user_pass': ''},
          {'ip_port': '218.73.128.119:32503', 'user_pass': ''},
          {'ip_port': '110.72.192.218:8123', 'user_pass': ''},
          {'ip_port': '182.42.244.111:808', 'user_pass': ''},
          {'ip_port': '180.121.129.106:808', 'user_pass': ''},
          {'ip_port': '171.12.139.198:20406', 'user_pass': ''},
          {'ip_port': '115.203.219.202:42847', 'user_pass': ''},
          {'ip_port': '110.72.16.15:8123', 'user_pass': ''},
          {'ip_port': '1.194.133.198:808', 'user_pass': ''},
          {'ip_port': '115.203.199.66:24560', 'user_pass': ''},
          {'ip_port': '60.182.238.66:32050', 'user_pass': ''},
          {'ip_port': '27.154.145.29:31839', 'user_pass': ''},
          {'ip_port': '49.85.3.53:34498', 'user_pass': ''},
          {'ip_port': '115.46.73.30:8123', 'user_pass': ''},
          {'ip_port': '117.95.199.86:44606', 'user_pass': ''},
          {'ip_port': '222.85.39.162:808', 'user_pass': ''},
          {'ip_port': '117.93.1.101:40268', 'user_pass': ''},
          {'ip_port': '180.120.215.107:3128', 'user_pass': ''},
          {'ip_port': '113.128.28.39:48452', 'user_pass': ''},
          {'ip_port': '49.83.24.179:808', 'user_pass': ''},
          {'ip_port': '221.229.18.196:3128', 'user_pass': ''},
          {'ip_port': '112.228.133.145:8118', 'user_pass': ''},
          {'ip_port': '113.105.203.221:3128', 'user_pass': ''},
          {'ip_port': '115.203.205.156:35039', 'user_pass': ''},
          {'ip_port': '221.229.18.103:3128', 'user_pass': ''}
          ]
