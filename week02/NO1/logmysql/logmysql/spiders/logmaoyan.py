# -*- coding: utf-8 -*-
import scrapy

from logmysql.items import LogmysqlItem
from scrapy.selector import Selector

class LogmaoyanSpider(scrapy.Spider):
    name = 'logmaoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=1']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3&sortId=1'
        yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        try:
            #打印网页的url
            print(response.url)
            # 打印网页的内容
            # print(response.text)
            i = 1
            movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
            for movie in movies:
                if i < 11:
                    # 路径使用 / .  .. 不同的含义　
                    filmname = movie.xpath('./div/span[@class="name "]/text()').extract_first()
                    filmtype =movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
                    plandate = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
                    # link = movie.xpath('./a/@href')
                    print('-----------')
                    print(filmname)
                    print(filmtype)
                    print(plandate)
                    print(i)
                    # print(link)
                    print('-----------')
                    item = LogmysqlItem()
                    item['filmid'] = i
                    item['filmname'] = filmname
                    item['filmtype'] = filmtype
                    item['plandate'] = plandate
                    i = i + 1
                    yield item
                else:
                    yield
        except Exception as e:
            print(e)  # 输出异常信息
