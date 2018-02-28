# -*- coding: utf-8 -*-
import scrapy
import time
from www_zhipin_com_test.items import WwwZhipinComTestItem

class ZhipinSpider(scrapy.Spider):
    # spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。 name是spider最重要的属性，而且是必须的

    name = 'zhipin'
    allowed_domains = ['www.zhipin.com']

    # URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。
    # 这里我们进行了指定，所以不是从这个 URL 列表里爬取
    start_urls = ['http://www.zhipin.com/']

    # 要爬取的页面，可以改为自己需要搜的条件，这里搜的是 上海-PHP，其他条件都是不限
    positionUrl = 'https://www.zhipin.com/c100010000/h_101280600/?query=python'
    curPage = 1
    # 发送 header，伪装为浏览器
    headers = {
        'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        'cookie': " __c=1519823275; __l=r=https%3A%2F%2Fwww.zhipin.com%2F&l=%2Fwww.zhipin.com%2Fc101010100-p100101%2F; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F1417416546.html%3Fka%3Dsearch_list_4; lastCity=101280600; __a=14181100.1519823031.1519823031.1519823275.53.2.52.53; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1519832062",
        'cache-control': "no-cache",
        'Referer': "https://www.zhipin.com/job_detail/?query=python&scity=101280600&industry=&position=",
        'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831"
    }

    # 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
    # 该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。
    def start_requests(self):
        return [self.next_request()]

    def parse(self, response):
        print("request -> " + response.url)
        job_list = response.css('div.job-list > ul > li')
        for job in job_list:
            item = WwwZhipinComTestItem()

            print(" =================== \n", job.extract(), " =================== \n")
            job_primary = job.css('div.job-primary')

            item['pid'] = job.css(
                'div.info-primary > h3 > a::attr(data-jobid)').extract_first().strip()
            item["positionName"] = job_primary.css(
                'div.info-primary > h3 > a::text').extract_first().strip()
            item["salary"] = job_primary.css(
                'div.info-primary > h3 > a > span::text').extract_first().strip()
            info_primary = job_primary.css(
                'div.info-primary > p::text').extract()
            print(info_primary)
            item['city'] = info_primary[0].strip()
            item['workYear'] = info_primary[1].strip()
            item['education'] = info_primary[2].strip()
            item['companyShortName'] = job_primary.css(
                'div.info-company > div.company-text > h3 > a::text'
            ).extract_first().strip()
            company_infos = job_primary.css(
                'div.info-company > div.company-text > p::text').extract()
            if len(company_infos) == 3:  # 有一条招聘这里只有两项，所以加个判断
                item['industryField'] = company_infos[0].strip()
                item['financeStage'] = company_infos[1].strip()
                item['companySize'] = company_infos[2].strip()

            publis_infos = job_primary.css(
                'div.info-publis > h3 > a::text').extract()
            print("publis_infos", publis_infos)
            # item['positionLables'] = job.css('li > div.job-tags > span::text').extract()
            # item['time'] = job.css('span.time::text').extract_first().strip()
            item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield item
        self.curPage += 1
        if self.curPage < 10:
            time.sleep(5)  # 停停停！听听听！都给我停下来听着！睡一会(～﹃～)~zZ
            yield self.next_request()

    def next_request(self):
        return scrapy.http.FormRequest(self.positionUrl + ("&page=%d&ka=page-%d" % (self.curPage, self.curPage)),
                                       headers=self.headers, callback=self.parse)

