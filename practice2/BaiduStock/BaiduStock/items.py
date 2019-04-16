# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidustockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    today = scrapy.Field()
    auction = scrapy.Field()
    max_ = scrapy.Field()
    stop = scrapy.Field()


class IPLocationItem(scrapy.Item):
    ip_location = scrapy.Field()
