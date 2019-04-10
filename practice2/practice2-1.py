# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# 空气质量数据可视化

import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 读取数据
data = pd.read_csv("pollution.csv")  # 默认header=True，首航作为列名
# 1-求PM2.5和气温日平均
# 数据预处理
years = list(set(data['year']))  # 年分表
months = list(range(1, 13))
# days = list(range(1, 32))
# every_day = [(m, d) for m in months for d in days ]
# # 求平均值，自动过滤NaN
# pm2d5_days = []
# temp_days = []
# for y in years:
#     # 每年的每个月有哪天
#     list(map(pm2d5_days.append, list(map(lambda x: data.loc[(data['year'] == y) & (data['month'] == x[0]) & (data['day'] == x[1]) & (data['pm2.5'].notnull())]['pm2.5'].mean(), every_day))))
#     list(map(temp_days.append, list(map(lambda x: data.loc[(data['year'] == y) & (data['month'] == x[0]) & (data['day'] == x[1]) & (data['TEMP'].notnull())]['TEMP'].mean(), every_day))))
# # 画图
# font = FontProperties(fname="C:\Windows\Fonts\msyh.ttc", size=15)  # 设置字体
# fig = plt.figure()  # 创建子图
# pm2d5_ax = fig.add_subplot(2, 1, 1)
# temp_ax = fig.add_subplot(2, 1, 2)
# bar_with = 0.5  # 柱状条宽度
# index = np.arange(len(years)* len(months) * len(days))  # 下标序列
# pm2d5_ax.bar(index, pm2d5_days, bar_with, label='PM2.5')
# temp_ax.bar(index, temp_days, bar_with, label='TEMP')
# # 标题
# pm2d5_ax.set_title(u'每年pm2.5日平均统计表', fontproperties = font)
# temp_ax.set_title(u'每年气温日平均统计表', fontproperties = font)
# pm2d5_ax.set_xlabel(u'日期', fontproperties = font)
# pm2d5_ax.set_ylabel(u'平均值', fontproperties = font)
# temp_ax.set_xlabel(u'日期', fontproperties = font)
# temp_ax.set_ylabel(u'平均值', fontproperties = font)
# pm2d5_ax.set_xticks([])
# temp_ax.set_xticks([])
# plt.show()
# plt.close()
pm2d5_y_avg = []  # pm2.5各年平均值
temp_y_avg = []  # 气温各年平均值
list(map(pm2d5_y_avg.append, list(map(lambda x: data.loc(data['year'] == x)['pm2.5'].mean(), years))))
list(map(temp_y_avg.append, list(map(lambda x: data.loc(data['year'] == x)['TEMP'].mean(), years))))
# 画图
font = FontProperties(fname="C:\Windows\Fonts\msyh.ttc", size=15)  # 设置字体
index = np.arange(len(years))
bar_width = 0.35
plt.bar(index, pm2d5_y_avg, bar_width, label='pm2.5')
plt.bar(index + bar_width, temp_y_avg, bar_width, label='temp')
plt.title(u"pm2.5和气温年日平均", fontproperties = font)
plt.xticks(index, years)
plt.ylabel(u"日均值", fontproperties = font)

# 2-求五年的PM2.5,气温，气压，累计降雨量趋势图
# 数据预处理,清除NA
pm2d5_data = data.loc[data['pm2.5'].notnull()]  # isnull()和notnull()返回布尔型
temp_data = data.loc[data['TEMP'].notnull()]
pres_data = data.loc[data['PRES'].notnull()]
iws_data = data.loc[data['Iws'].notnull()]
# 画图
fig = plt.figure()
# 添加子图
pm2d5_ax = fig.add_subplot(2, 2, 1)
temp_ax = fig.add_subplot(2, 2, 2)
pres_ax = fig.add_subplot(2, 2, 3)
iws_ax = fig.add_subplot(2, 2, 4)
# 向子图中添加数据
pm2d5_ax.plot(pm2d5_data['pm2.5'], "-", linewidth=0.2)
temp_ax.plot(temp_data['TEMP'], "-", linewidth=0.2)
pres_ax.plot(pres_data['PRES'], "-", linewidth=0.2)
iws_ax.plot(iws_data['Iws'], "-", linewidth=0.2)
# 隐藏x轴刻度
pm2d5_ax.set_xticks([])
temp_ax.set_xticks([])
pres_ax.set_xticks([])
iws_ax.set_xticks([])
# 设置标题
pm2d5_ax.set_title('pm2.5')
temp_ax.set_title('TEMP')
pres_ax.set_title('PRES')
iws_ax.set_title('Iws')
plt.show()
plt.close()

# 3-统计每年PM2.5指数平均值最高的5个月，获取每天的PM2.5指数
# 数据预处理
pm2d5_m_avg = []
for m in months:
    # 每年的m月平均pm2.5，注意筛选条件用括号分隔避免歧义(ambiguous)
    pm2d5_m_avg.append(list(map(lambda x: (m, data.loc[(data['year'] == x) & (data['month'] == m) & (data['pm2.5'].notnull())]['pm2.5'].mean()), years)))
# 转置结果，
pm2d5_m_avg_T = [[row[col] for row in pm2d5_m_avg] for col in range(len(pm2d5_m_avg[0]))] # 转置
# 进行每年的前五排序切片
pm2d5_m_avg_top5 = list(map(lambda x: sorted(x, key=lambda x: x[1], reverse=True)[:5], pm2d5_m_avg_T))
# 按升序排列月份以便计算
pm2d5_m_avg_top5 = list(map(lambda x: sorted(x, key=lambda x: x[0]), pm2d5_m_avg_top5))
pm2d5_d_data = []
for i, l in enumerate(pm2d5_m_avg_top5):  # 筛选每年每月的数据[y:[m:...], y:[m:...]...]
    pm2d5_d_data.append(list(map(lambda x: data.loc[(data['year'] == years[i]) & (data['month'] == x[0]) & (data['pm2.5'].notnull())], l)))
# 画图
plt.rcParams['figure.figsize'] = (10.0, 1.0) # 图片长宽比例
plt.rcParams['savefig.dpi'] = 500  # 图片像素
plt.rcParams['figure.dpi'] = 400  # 分辨率

for n, dl in enumerate(pm2d5_d_data):  # 按一年组建x, y坐标
    x_data = []
    y_data = []
    for e in dl:
        # x为时间(天)
        list(map(x_data.append,list(map(lambda y, m, d, h: str(datetime.datetime(int(y), int(m), int(d), int(h))), e['year'], e['month'], e['day'], e['hour']))))
        # y为PM2.5值
        list(map(y_data.append, list(e['pm2.5'])))
    plt.plot(x_data, y_data, "-", linewidth=0.2)
plt.xticks([])  # 隐藏x轴刻度
plt.yticks(range(0, 1200, 50))  # 设置y轴刻度
plt.tick_params(labelsize=3)  # 设置刻度字体大小
plt.show()
plt.close()