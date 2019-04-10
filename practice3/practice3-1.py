# -*-coding:utf-8-*-
# created by HOlyKwok 201610414206
# 多元线性回归预测汽车的油耗（公里/加仑）

import pandas as pd
import matplotlib as plt


car_attrbution = ['mpg', 'cylinders', 'displacement',
                  'horsepower', 'weight', 'acceration',
                  'model-year', 'origin', 'car-name']
# 装载数据
cars = pd.read_table('auto-mpg.data', delim_whitespace=True, names=car_attrbution)
print(cars.head(2))
print(type(cars['mpg']))
# 特征提取
feature_cols = ['cylinders', 'displacement', 'weight', 'acceration']
x_data = cars[feature_cols]
print(type(x_data.loc[0, 'cylinders']))  # 查看第一行的此属性的数据类型，之后需要使用矩阵，需要确定是否为浮点数
# 数据类型转换
try:
    x_data['cylinders'] = x_data['cylinders'].astype('float64')
    x_data['displacement'] = x_data['displacement'].astype('float64')
    x_data['weight'] = x_data['weight'].astype('float64')
    x_data['acceration'] = x_data['acceration'].astype('float64')
except:
    pass
y_data = cars['mpg']
print(type(x_data.loc[0, 'cylinders']))
# 构造训练集和测试集
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, random_state=1)
# 建立线性回归模型
from sklearn.linear_model import LinearRegression
linereg = LinearRegression()
# 训练
model = linereg.fit(x_train, y_train)
# 查看模型
# 预测
y_pred = linereg.predict(x_test)
print(y_pred)
# 算法评价
from sklearn import metrics
import numpy as np
sum_mean = 0
for i in range(len(y_pred)):
    sum_mean += (y_pred - y_test.values[i])**2
sum_erro = np.sqrt(sum_mean/len(y_pred))
print("RMSE:", sum_erro)
# 结果可视化
import matplotlib.pyplot as plt
plt.figure()
# 画x,y