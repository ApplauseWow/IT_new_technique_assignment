# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# 统计电影工作人员
# practice1-9

import numpy as np


def static_num(top_dic, who):
    """
    统计参与数
    :param top_dic: 统计表
    :param who: 统计对象
    :return: none
    """

    top_dic[who] = top_dic.get(who, 0) + 1


def list_top(statistic_list):
    """
    显示统计结果
    :param statistic_list:  统计的列表
    :return: none
    """

    sorted_list = sorted(statistic_list.items(), key=lambda x: x[1], reverse=True)
    if_more = list(filter(lambda x: sorted_list[0][1] == x[1], sorted_list))
    for i in if_more:
        print(i[0], "最多", ">>>共:", i[1], "部")


movie_info = list()  # 电影职员表
# 读取数据, 构建职员表
with open('movie_staff', 'r') as f:
    lines = f.readlines()  # 按行读取所有内容
    for line in lines:  # 读取每一行
        line = line.split()
        movie_info.append(line)

# 统计导演作品最多导演和参演最多的演员
conduct_num = dict()  # 导演电影数
actor_num = dict()  # 参演数
actor_list = list()  # 演员表
for l in movie_info:  # 遍历每一部电影
    static_num(conduct_num, l[1])  # 统计导演作品数
    # 与python2不同python3的map()与filter返回iterator
    '''map -> Make an iterator that computes the function using arguments from each of the iterables. 
    Stops when the shortest iterable is exhausted.'''
    # 此时iterator还没有开始遍历，需要一个能够调用__next__()的对象
    list(map(lambda x: static_num(actor_num, x), l[2:]))  # 统计演员参演数
    list(map(actor_list.append, [a for a in l[2:] if a not in actor_list]))  # 生成演员表['a1', 'a2'，...]

# 统计共同参演最多的两位演员
# 构成无向图的邻接矩阵，对称的
# 与python2不同python3numpy.zeros参数需要提供一个seq序列，不再是单个参数
matrix = np.zeros((len(actor_list), len(actor_list)))  # 生成邻接矩阵
# matrix = [[0 for i in range(len(actor_list))] for j in range(len(actor_list))]
for l in movie_info:
    actor_couple = [(x, y) for x in l[2:] for y in l[2:] if x is not y and actor_list.index(x) < actor_list.index(y)]  # 构成不重复的此部电影同台演员组合并且按照演员表索引前后顺序配对，即(1,2)不会(2,1)

    def add_one(couple):  # 创建一个闭包函数用于map
        matrix[actor_list.index(couple[0])][actor_list.index(couple[1])] += 1
    list(map(add_one, actor_couple))  # 统计共同参演数

list_top(conduct_num)  # 展示统计导演作品最多结果
list_top(actor_num)  # 展示统计演员参演最多结果
# print(matrix)  # 展示共同参演结果
top_couple = max([max(a) for a in matrix])  # 最多的共同参演数
couples = np.argwhere(matrix == top_couple)  # 找出等于最大值的所有索引
# print(type(couples), couples[0][0], couples[0][1])
for c in couples:  # 展示共同参演最多的组合
    print(actor_list[c[0]], "和", actor_list[c[1]], "最多")