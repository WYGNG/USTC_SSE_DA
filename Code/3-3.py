# 代码3-3 捞起生鱼片的季度销售情况
import pandas as pd
import numpy as np
catering_sale = '../data/catering_fish_congee.xls'  # 餐饮数据
data = pd.read_excel(catering_sale,names=['date','sale'])  # 读取数据，指定“日期”列为索引

bins = [0,500,1000,1500,2000,2500,3000,3500,4000]
labels = ['[0,500)','[500,1000)','[1000,1500)','[1500,2000)',
       '[2000,2500)','[2500,3000)','[3000,3500)','[3500,4000)']

data['sale分层'] = pd.cut(data.sale, bins, labels=labels)
aggResult = data.groupby(by=['sale分层'])['sale'].agg({'sale': np.size})

pAggResult = round(aggResult/aggResult.sum(), 2, ) * 100

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))  # 设置图框大小尺寸
pAggResult['sale'].plot(kind='bar',width=0.8,fontsize=10)  # 绘制频率直方图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.title('季度销售额频率分布直方图',fontsize=20)
plt.show()
