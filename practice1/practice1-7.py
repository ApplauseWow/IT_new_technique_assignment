# -*-coding::utf-8-*-
# created by HolyKwok 201610414206
# practice1-7

# 01-knapsack problem

all_w = 8 # 最大背包承重
weight = [0, 4, 5, 2, 1, 6] # 物品重量 
value = [0, 45, 57, 22, 11, 67] # 物品价值
value_list = [[0 for i in range(all_w + 1)] for j in range(len(value))] # 规划图
# 生成物品映射
letters = [0]
letters.extend([chr(letter) for letter in range(ord('A'), ord('Z') + 1)])
good_dict = {}
for i in range(len(weight)):
    good_dict[i] = letters[i]
got_list = [False for i in range(len(weight))] # 拿去物品列表

for w in range(1, all_w + 1): # 当前背包所剩余容量，当前容量考虑n个物品时最多能放多少
    for n in range(1, len(value)): # 考虑第n个物品
        if weight[n] <= w: # 当前物品能装进去，不管上一个物品是如何装进去装的是什么
            value_list[n][w] = max(value_list[n - 1][w - weight[n]] + value[n], value_list[n - 1][w]) # 放后与放前的价值比较
        else: # 不能放进去，不用考虑
            value_list[n][w] = value_list[n - 1][w]
import numpy as np
print("规划表：\n", np.array(value_list))

r = 0
c = 0
max_val = max([max(x) for x in value_list]) # 最大值
for i in value_list: # 找到最大值所在位置
    if max_val in i:
        r = value_list.index(i) 
        c = i.index(max_val)
    else:
        pass

while True:
    if value_list[r][c] == 0: # 找完
        break
    else: # 继续找
        if value_list[r][c] - value[r] != value_list[r - 1][c - weight[r]]:# 没有拿第r个物品
            r -= 1
        else: # 拿了第r个物品
            got_list[r] = True
            c -= weight[r]
            r -= 1
print([good_dict[y] for y in [x for x, y in enumerate(got_list) if y is True]]) # 拿取结果

