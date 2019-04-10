# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:41:01 2019

@author: hdk
"""


import requests

from bs4 import BeautifulSoup

import re

 

def getHTMLText(url, code="utf-8"):

    try:

        r = requests.get(url)

        r.raise_for_status()#抛出异常

        r.encoding = code#设定编码格式

        return r.text

    except:

        return ""

 

def getStockList(lst, stockURL):

    html = getHTMLText(stockURL, "GB2312")  #只获取htlm文本

    soup = BeautifulSoup(html, 'html.parser') #html解析，到这里把整个网站源代码排版整理干净

    a = soup.find_all('a')     #解析页面，找到所有的a标签

    for i in a:

        #a[1] =<a href="http://finance.eastmoney.com/yaowen.html" target="_blank">要闻</a>

        #type(a[1]) = bs4.element.Tag

        try:

            #找到a标签中的href属性，并且判断属性中间的链接，把链接后面的数字取出来

            href = i.attrs['href']

            #a[1].attrs['href'] = 'http://finance.eastmoney.com/yaowen.html'

            #深圳交易所的代码以sz开头，上海交易所的代码以sh开头，股票的数字有6位构成，所以正则表达式可以写为[s][hz]\d{6}

            lst.append(re.findall(r"[s][hz][_]\d{6}", href)[0].replace('_',''))

        except:

            #try...except来对程序进行异常处理

            continue

 

def getStockInfo(lst, stockURL, fpath):

    count = 0

    for stock in lst:

        url = stockURL + stock + ".html"

        html = getHTMLText(url)#对一只股票进行操作

        try:

            if html=="":

                continue

            infoDict = {}

            soup = BeautifulSoup(html, 'html.parser')

            stockInfo = soup.find('div',attrs={'class':'stock-bets'})#find整理成以<div class="stock-bets">的整段代码

#            <div class="stock-bets">

#            <h1>

#            <a class="bets-name" href="/fund/sh500038.html">

#                        基金通乾 (<span>500038</span>)

#                        </a>

#            <span class="state f-up">已休市 2018-07-20 15:01:32

#                        </span>

#            </h1>

#            <div class="price s-stop ">

#            <strong class="_close">0.94</strong>

#            <span>--</span>

#            <span>0.00%</span>

#            </div>

#            <div class="bets-content">

#            <div class="bets-col-8">

#            <dl><dt>最高</dt><dd class="s-down">--</dd></dl>

#            <dl><dt>最低</dt><dd class="s-down">--</dd></dl>

#            <dl><dt>今开</dt><dd class="">--</dd></dl>

#            <dl><dt>昨收</dt><dd>0.94</dd></dl>

#            <dl><dt>成交额</dt><dd>--</dd></dl>

#            <dl><dt>成交量</dt><dd>--</dd></dl>

#            <dl><dt>净值</dt><dd>0.9515</dd></dl>

#            <dl><dt>折价率</dt><dd>-1.42</dd></dl>

#            </div>

#            <div class="clear"></div>

#            </div>

#            </div>

 

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]#find_all从所有的stockInfo取出name

#            <a class="bets-name" href="/fund/sh500038.html">

#            基金通乾 (<span>500038</span>)

#            </a>

            infoDict.update({'股票名称': name.text.split()[0]})

#            text取出<a class="bets-name" href="/fund/sh500038.html"> (<span> </span>)  </a> 标签代码以外文本

#            

#            股票的其他信息存放在dt和dd标签中，其中dt表示股票信息的键域，dd标签是值域。获取全部的键和值：

            keyList = stockInfo.find_all('dt')

 

            valueList = stockInfo.find_all('dd')

            for i in range(len(keyList)):

                key = keyList[i].text#text可直接在<dt>最高</dt>提取

                val = valueList[i].text#text可直接在<dd>0.94</dd>提取

                infoDict[key] = val#值赋到字典的键中

 

            with open(fpath, 'a', encoding='utf-8') as f:

                f.write( str(infoDict) + '\n' )

                count = count + 1

                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")

        except:

            count = count + 1

            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")

            continue

 

if __name__=="__main__":
     #stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_list_url = 'http://quote.stockstar.com/stock/stock_index.htm'

    stock_info_url = 'https://gupiao.baidu.com/stock/'

    output_file = 'BaiduStockInfo-RE.txt'

    slist=[]

    getStockList(slist, stock_list_url)

    getStockInfo(slist, stock_info_url, output_file)
