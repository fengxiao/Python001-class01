# -*- coding: utf-8 -*-
import scrapy

from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    #allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=1']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3&sortId=1'
        yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        #打印网页的url
        print(response.url)
        # 打印网页的内容
        # print(response.text)
        i = 0
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            if i < 10:
                # 路径使用 / .  .. 不同的含义　
                filmname = movie.xpath('./div/span[@class="name "]/text()').extract_first()
                filmtype =movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
                plandate = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
                # link = movie.xpath('./a/@href')
                i = i + 1
                print('-----------')
                print(filmname)
                print(filmtype)
                print(plandate)
                print(i)
                # print(link)
                print('-----------')
                item = MaoyanmovieItem()
                item['filmname'] = filmname
                item['filmtype'] = filmtype
                item['plandate'] = plandate
                yield item
            else:
                yield
