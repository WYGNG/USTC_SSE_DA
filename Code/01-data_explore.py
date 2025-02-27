#-*- coding: utf-8 -*- 

# 代码7-1

# 对数据进行基本的探索
# 返回缺失值个数以及最大最小值

import pandas as pd

datafile= '../data/air_data.csv'  # 航空原始数据,第一行为属性标签
resultfile = '../tmp/explore.csv'  # 数据探索结果表

# 读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
data = pd.read_csv(datafile, encoding = 'utf-8')

# 包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）
explore = data.describe(percentiles = [], include = 'all').T  # T是转置，转置后更方便查阅
explore['null'] = len(data)-explore['count']  # describe()函数自动计算非空值数，需要手动计算空值数

explore = explore[['null', 'max', 'min']]

explore.columns = [u'空值数', u'最大值', u'最小值']  # 表头重命名

'''
这里只选取部分探索结果。
describe()函数自动计算的字段有count（非空值数）、unique（唯一值数）、top（频数最高者）、
freq（最高频数）、mean（平均值）、std（方差）、min（最小值）、50%（中位数）、max（最大值）
'''

#必须要encoding不然csv文件就会乱码
explore.to_csv(resultfile,encoding="utf_8_sig")  # 导出结果
