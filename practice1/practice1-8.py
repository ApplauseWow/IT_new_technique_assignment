# -*-coding:utf-8-*-
import re
import wordcloud
import collections
import jieba
from PIL import Image
from numpy import array
import matplotlib.pyplot as plt

# 名词复数和原型如何解决？？？
top = 20  # 前n名

# 读取文本
with open('article.txt') as f:
    article = f.read()  # 内容开头有乱码？？？

# 处理文本
article.lower()  # 所有换成小写, lower失败？？？
patten = re.compile(u'\n|\t|\.|-|:|,|;|\(|\)|\'|\"|\?|!|')  # 建立模式
article = re.sub(patten, '', article)   # 去掉模式中的字符

# 文本分词
segment_list = jieba.cut(article)  # 分词
remain_words = [] # 去掉无关词汇的分词结果列表
remove_words = ['i', 'you', 'he', 'she', 'his', 'her', 'my', 'the', 'this', 'that', 'those', 'these',
                'am', 'is', 'are', 'were', 'was', 'have', 'had', 'haven', 'a', 'an', 'it', 'its',
                'what', 'why', 'how', 'when', 'where', 'yours', 'mine', 'from', 'here', 'there', 'say', 'said', 'ask',
                'and', 'or', 'about', 'us', 'we', 'they', 'our', 'ours', 'them', 'then', ' ', 'of', 'to', 'with', 'in',
                'on', 'up', 'down', 'by', 'use', 'out', 'as', 'be', 'has', 'their', 'can', 'Can', 'for', 'such', 'as'
                ]  # 无关词汇
for word in segment_list:
    if word not in remove_words:
        word.lower()
        remain_words.append(word)  # 添加有效词汇

# 统计词频
word_count = collections.Counter(remain_words)  # 创建统计实例
word_top = word_count.most_common(top)  # 统计前top个词汇

# 生成词云
mask = array(Image.open('mask.jpg')) # 生成词云轮廓
word_cloud = wordcloud.WordCloud(mask=mask, max_words=top, max_font_size=500, background_color="black")  # 词云样式
word_cloud.generate_from_frequencies(word_count)  # 从字典生成
# word_cloud.generate_from_text()
# word_cloud.generate()
plt.imshow(word_cloud)  # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图像
