# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# 百度股票爬虫
from bs4 import BeautifulSoup
import re
import requests


# 获取网页源码
def get_html(url, code='utf-8'):
    """
    基本抓取网页框架
    url: protocol://url
    """

    try:
        html_content = requests.get(url, timeout=20)  # 设置超时
        html_content.raise_for_status()
        # html_content.encoding = html_content.apparent_encoding
        html_content.encoding = code
        return html_content.text
    except:
        print('页面访问异常！')
        return ""


# 获取股票代码，存放于slist
def get_stock_list(slist, stock_list_url):
    """
    slist: 股票代码列表
    stock_list_url: 股票url
    """

    html = get_html(stock_list_url)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a', href=re.compile("^/gs/*"))  # 寻找匹配标签
    for i in a:
        try:
            href = i.attrs['href']  # 提取标签中的属性
            temp = re.findall(r's[hz]_\d{6}', href)[0]  # 原生的字符串，不将转移符视为转移符 r' ' ,返回匹配列表，只取第一个
            temp = temp.replace('_', '')
            slist.append(temp)
        except:
            continue  # 没有直接略过


# 以此获取股票交易信息，存放到output_file
def get_stock_info(slist, stock_info_url, output_file):
    """
    slist:
    stock_info_url:
    output_file:
    """

    count = 0
    for stock_code in slist:
        count += 1  # 进度条
        # 组成URL
        stock_info_html = get_html("".join((stock_info_url, stock_code, '.html')))



if __name__ == '__main__':
    stock_list_url = 'http://quote.stockstar.com/stock/stock_index.html'
    stock_info_url = 'gupiao.baidu.com/stock/'
    slist = []  # 股票代码列表
    file_path = './stocks.txt'  # 输出文件路径
    get_stock_list(slist, stock_list_url)  # 获取股票代码
    get_stock_info(slist, stock_info_url, file_path)  # 爬取股票信息