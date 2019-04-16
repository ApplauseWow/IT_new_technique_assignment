# -*- coding: utf-8 -*-
import scrapy
from BaiduStock.items import IPLocationItem


class IpLocationSpider(scrapy.Spider):

    name = 'ip_location'
    allowed_domains = ['ip138.com']  # 过滤爬取的网页域名，但不过滤start_url
    start_urls = ['http://m.ip138.com/ip.asp?ip=www.applausewow.cn']  # 待修改超链接

    def parse(self, response):
        result = response.css("p.result::text").extract()[0].split("：")[1]
        ip_location = IPLocationItem()
        if result:
            ip_location['ip_location'] = result
            yield ip_location
        else:
            print("no result...")
