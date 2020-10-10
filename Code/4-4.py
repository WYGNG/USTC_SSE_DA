import pandas as pd
import numpy as np

datafile = 'normalization_data.xls' #参数初始化
data = pd.read_excel(datafile, header = None) #读取数据
#print(data)

min_max = (data - data.min())/(data.max() - data.min()) #最小-最大规范化
#print(min_max)
ling_mean = (data - data.mean())/data.std() #零-均值规范化
#print(ling_mean)
demi = data/10**np.ceil(np.log10(data.abs().max())) #小数定标规范化
