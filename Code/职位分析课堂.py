import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
data = pd.read_csv('../data/job_info.csv', encoding='GBK', header=None, index_col=0)
data.index = range(len(data))
data.columns = ['公司名','岗位名','工作地点','工资','发布日期','工作描述','公司类型','公司规模','行业']

#去重
print('\n 去重前%s条数据：', data.shape)
data.drop_duplicates(subset=['公司名','岗位名'], inplace=True)
print('\n 去重后%s条数据：', len(data))

#岗位名
data['岗位名']=data['岗位名'].str.strip().apply(lambda x : x.lower())
data['岗位名'].value_counts()
pd.set_option('display.max_rows', 20)
target_job = ['算法', '分析', '工程师', '开发', '数据', '运营', '运维']    # 目标岗位
index=[data['岗位名'].str.count(i) for i in target_job]
np.array(index)
np.array(index).shape
index=np.array(index).sum(axis=0)>0
job_info=data[index]
job_info.shape

job_list = ['数据分析', '数据挖掘', '算法', '大数据',
            '开发工程师', '运营', '软件工程', '前端开发',
            '深度学习', 'AI', '数据库', '数据产品',
            '客服', 'java', '.net', 'andriod', '人工智能', 'c++',
            '数据管理']#列表形式
x = '数据分析与算法'
job_list=np.array(job_list)
index=[i in x for i in job_list]
x=job_list[index][0]
def rename_job(x=None, namelist= job_list):
    index = [i in x for i in namelist]
    if sum(index)>0:
        return  namelist[index][0]
    else:
        return x

rename_job(x)
job_info['岗位名']=job_info['岗位名'].apply(rename_job)
a=job_info['岗位名'].value_counts()[:10]
plt.rcParams['font.sans-serif'] = 'SimHei'
a.plot(kind='bar')
plt.title('热门招聘岗位')
plt.show()

#工作地点
job_info['工作地点'].value_counts()
address_list = ['北京', '上海', '广州', '深圳', '杭州', '苏州', '长沙',
                '武汉', '天津', '成都', '西安', '东莞', '合肥', '佛山',
                '宁波', '南京', '重庆', '长春', '郑州', '常州', '福州',
                '沈阳', '济南', '宁波', '厦门', '贵州', '珠海', '青岛',
                '无锡', '大连','哈尔滨','昆明','南昌']#大数据岗位常见城市名
address_list=np.array(address_list)
def rename_address(x=None, namelist= address_list):
    index = [i in x for i in namelist]
    if sum(index)>0:
        return  namelist[index][0]
    else:
        return x
job_info['工作地点']=job_info['工作地点'].apply(rename_address)
a=job_info['工作地点'].value_counts()[:10]

plt.rcParams['font.sans-serif'] = 'SimHei'
a.plot(kind='bar')
plt.title('热门工作城市')
plt.show()

#工资
job_info['工资'].str[-1].value_counts()
job_info['工资'].str[-3].value_counts()
index1=job_info['工资'].str[-1].apply(lambda x : x in ['年','月'])
index2=job_info['工资'].str[-3].apply(lambda x : x in ['万','千'])
job_info=job_info[index1 & index2]
job_info.shape

y='1-1.5万/年'
re.findall('\d+\.?\d*',y)
def gongzi(x=None):
    try:
        if x[-3] == '万':
            a=[float(i)*10000 for i in re.findall('\d+\.?\d*',x)]
        elif x[-3] == '千':
            a = [float(i) * 1000 for i in re.findall('\d+\.?\d*', x)]
        if x[-1] =='年':
            a = [i/12 for i in a]
        return a
    except:
        return x
gongzi(y)
salary = job_info['工资'].apply(gongzi)
job_info['最低工资'] = salary.str[0]
job_info['最高工资'] = salary.str[1]
job_info['工资水平'] = job_info[['最低工资', '最高工资']].mean(axis=1)

#公司类型
job_info['公司类型'].value_counts()
job_info['公司类型'].str[1]
#index = job_info['公司类型'].apply(lambda x : len(x)<6)
#job_info.loc[index,'公司类型'] = np.nan
job_info.loc[job_info['公司类型'].apply(lambda x : len(x)<6), '公司类型'] =np.nan
job_info['公司类型'] = job_info['公司类型'].str[2:-2]
job_info['公司类型'].value_counts()

#行业
job_info['行业'].value_counts()
job_info.loc[job_info['行业'].apply(lambda x : len(x)<6), '行业'] =np.nan
job_info['行业'] = job_info['行业'].str[2:-2].str.split(',').str[0]
job_info['行业'].value_counts()

a=job_info['行业'].value_counts()[:10]
plt.rcParams['font.sans-serif'] = 'SimHei'
a.plot(kind='bar')
plt.subplots_adjust(bottom=0.2)
plt.xticks(rotation=45)
plt.title('热门招聘行业')
plt.show()

#可视化热门岗位的工资
a=job_info.groupby('岗位名').agg({'工资水平': 'mean','公司名': 'count'}).sort_values('公司名', ascending=False)
b=a['工资水平'][:10]
plt.rcParams['font.sans-serif'] = 'SimHei'
b.plot(kind='bar')
plt.subplots_adjust(bottom=0.2)
plt.xticks(rotation=45)
plt.title('热门招聘岗位的工资')
plt.show()
