# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# 百度股票爬虫和IP地址归属地自主查询
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd


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
    today = []  # 今开
    auction = []  # 成交量
    max_ = []  # 最高
    stop = []  # 涨停
    for stock_code in slist:
        # 组成URL
        url = "".join((stock_info_url, stock_code, '.html'))
        stock_info_html = get_html(url)
        try:
            soup = BeautifulSoup(stock_info_html, 'html.parser')
            div = soup.find_all('div', class_="line1")[0]  # 寻找匹配标签, find_all返回ResultSet
            list(map(lambda x, y: x.append(y.text), [today, auction, max_, stop], div.find_all('dd')[:5]))
            count += 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(slist)), end="")
        except:
            count += 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(slist)), end="")
            continue
    column_today = pd.Series(today, name='today')
    column_auction = pd.Series(auction, name='auction')
    column_max = pd.Series(max_, name='max')
    column_stop = pd.Series(stop, name='stop')
    save = pd.DataFrame({'today': column_today, 'auction': column_auction, 'max': column_max, 'stop': column_stop})
    save.to_csv(output_file, index=False, sep=' ')


def find_host_location(ip):
    """
    IP地址归属地自主查询
    :param url: ip 或者 域名
    :return: a dict of location information
    """

    url = "".join(("http://m.ip138.com/ip.asp?ip=", ip))
    html = get_html(url)
    try:
        soup = BeautifulSoup(html, "html.parser")
        p = soup.find_all("p", class_="result")
        return p
    except:
        print("no result...")


if __name__ == '__main__':
    # 股票信息
    # stock_list_url = 'http://quote.stockstar.com/stock/stock_index.html'
    # stock_info_url = 'http://gupiao.baidu.com/stock/'
    # slist = []  # 股票代码列表
    # file_path = 'stocks.csv'  # 输出文件路径
    # get_stock_list(slist, stock_list_url)  # 获取股票代码
    # get_stock_info(slist, stock_info_url, file_path)  # 爬取股票信息

    # ip地址归属地
    location = find_host_location('www.applausewow.cn')
    print(location[0].text)