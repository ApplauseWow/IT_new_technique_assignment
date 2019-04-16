# -*- coding: utf-8 -*-
import scrapy
import re
from BaiduStock.items import BaidustockItem
import random

class StockSpider(scrapy.Spider):
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]
    name = 'stock'
    allowed_domains = ['baidu.com']  # 过滤爬取的网页域名，但不过滤start_url
    start_urls = ['http://quote.stockstar.com/stock/stock_index.htm']  # 待修改超链接

    # 解析超文本
    def parse(self, response):
        all_css = response.css('a::attr(href)').extract()  # 提取a标签中的href属性，返回一个选择器的列表，然后在extract列表
        headers = headers = {
                    'Accept-Encoding': 'gzip, deflate, sdch, br',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Connection': 'keep-alive',
                    'Referer': 'https://gupiao.baidu.com/',
                    'User-Agent': random.choice(self.USER_AGENTS)
                }  # 构造请求头

        for attr in all_css:
            # 提取股票代码
            attr = re.findall(r'[s][hz]_\d{6}', attr)
            if attr:  # 不为空
                item = attr[0].replace("_", "")
                url = "".join(("http://gupiao.baidu.com/stock/", item, ".html"))
                yield scrapy.Request(url=url, callback=self.parse_info, headers=headers, meta={'item':item})
            else:
                continue

    def parse_info(self, response):
        stock_id = response.meta['item']
        all_css = response.css('div.line1 dd::text').extract()[:4]
        if all_css:
            stockInfo = BaidustockItem()
            stockInfo['id'] = stock_id
            stockInfo['today'] = all_css[0]
            stockInfo['auction'] = re.findall(re.compile(r"[0-9]*\.?[0-9]*"), all_css[1])[0]
            stockInfo['max_'] = all_css[2]
            stockInfo['stop'] = all_css[3]
            yield stockInfo
        else:
            pass