# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LogmysqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    filmname = scrapy.Field()
    filmtype = scrapy.Field()
    plandate = scrapy.Field()
    filmid = scrapy.Field()