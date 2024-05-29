#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/12/22 9:27
# @Author : Lucas
# @File : frequencyDirectDistributionPlot.py
from collections import Counter
import pandas as pd
from scipy.stats import norm
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 可以正常显示中文
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
plt.tight_layout() # 为了正常显示一些图表被遮盖或者不完全显示的问题
import random
import numpy as np

class frequencyDirectDistribution:
    def __init__(self,data,column_name):
        '''
        @:parameter data:属于一维数据，可以为列表，或者为series类型pandas数据
        @:parameter column_name:属于列名数据
        '''
        self.data = data
        self.column_name = column_name
        pass
    def draw_plot(self,storage_dir='./',sclaer_flag=False):
        fig, ax = plt.subplots()
        # 绘制频数曲线
        # counts, bins, _ = plt.hist(content[name].tolist(), bins=60, edgecolor='blue', density=True)
        data = list(self.data)
        name = self.column_name
        if isinstance(data[0], (float)):
            if sclaer_flag:
                # 数据标准化处理
                standard_data = np.array(data)
                standard_data = standard_data.reshape(-1, 1)
                standard_data = StandardScaler().fit_transform(standard_data)
                data = standard_data.reshape(-1)
            # 计算均值以及标准差
            mu = np.mean(data)
            sigma = np.std(data)
            counts, bins, _ = plt.hist(data, bins=60, edgecolor='blue', density=True)
            # 拟合一条最佳正态分布曲线y
            y = norm.pdf(bins, mu, sigma)
            # 绘制y的曲线
            ax.plot(bins, y, 'r--')
        elif isinstance(data[0], (int)):
            frequency_counter = Counter(data)
            # draw the Discrete variables frequency
            plt.bar(frequency_counter.keys(), frequency_counter.values(), edgecolor="black")
            values = list(frequency_counter.keys())
            frequencys = list(frequency_counter.values())
            # 在每个条形上显示数值
            for i, value in enumerate(values):
                plt.text(value, frequencys[i] + 0.1, str(frequencys[i]), ha='center', va='bottom')
        else:
            # 如果属于统计类型，直接绘制频数直方图
            counts, bins, _ = plt.hist(data, bins=60, edgecolor='blue')
        # 有关于xlabel坐标轴是否需要关闭
        # plt.xticks([])
        plt.title(name)
        plt.savefig('{}/{}.jpg'.format(storage_dir,name))
        plt.show()
if __name__ == "__main__":
    data = pd.read_csv('petrol_consumption.csv')
    column_name = "Petrol_tax"
    petrol_tax_data = data.loc[:, column_name]
    frequencyDirectDistribution = frequencyDirectDistribution(petrol_tax_data, column_name)
    frequencyDirectDistribution.draw_plot()