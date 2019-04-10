# -*- coding: utf-8 -*-
import scrapy
import re

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']  # 待修改超链接

    # 解析超文本
    def parse(self, response):
        allCss = response.css('a::attr(href)').extract()[0]  # 提取a标签中的属性
        for attr in allCss:
            # 提取股票代码
            attr = re.findall(r'[s][hz]_\d{6}', attr)