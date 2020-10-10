import pandas as pd
import numpy as np

job_list = ['数据分析', '数据挖掘', '算法', '大数据',
            '开发工程师', '运营', '软件工程', '前端开发',
            '深度学习', 'AI', '数据库', '数据产品',
            '客服', 'java', '.net', 'andriod', '人工智能', 'c++',
            '数据管理']  # 列表形式
target_job = ['算法', '分析', '工程师', '开发', '数据', '运营', '运维']  # 目标岗位

data = pd.read_csv('job_info.csv', header=None, encoding='GBK', index_col=0)
data.index = range(len(data))
data.columns = ['公司名', '岗位名', '工作地点', '工资', '发布日期', '职位描述', '公司类型', '公司规模', '行业']

# 去重
print('\n 去重前%s条数据:', data.shape)
data.drop_duplicates(subset=['公司名', '岗位名'], inplace=True)

print('\n 去重后%s条数据:', data.shape)

# 岗位名
data['岗位名'] = data['岗位名'].str.strip().apply(lambda x: x.lower())
data['岗位名'].value_counts()
pd.set_option('display.max_rows', None)

index = [data['岗位名'].str.count(i) for i in target_job]
index = np.array(index)

job_info = data[index.sum(axis=0) > 0]

x = '数据分析与算法'
job_list = np.array(job_list)
index = [i in x for i in job_list]
y = job_list[index]


def rename_job(x=None, nameList=job_list):
    index = [i in x for i in job_list]
    if sum(index) > 0:
        return nameList[index][0]
    else:
        return x


rename_job(x)
job_info['岗位名'] = job_info['岗位名'].apply(rename_job)
job_info['岗位名'].value_counts()


address_list = ['北京', '上海', '广州', '深圳', '杭州', '苏州', '长沙',
                '武汉', '天津', '成都', '西安', '东莞', '合肥', '佛山',
                '宁波', '南京', '重庆', '长春', '郑州', '常州', '福州',
                '沈阳', '济南', '宁波', '厦门', '贵州', '珠海', '青岛',
                '无锡', '大连','哈尔滨','昆明','南昌']#大数据岗位常见城市名

y='1-1.5万/月'

re.findall('\d+\.?d*',y)

def gongzi(x=None):
    try:
        if x[-3] == '万':
            a = [float(i)*1000 for i in re.findall('\d+\.?d*',x)]
        elif x[-3] == '千':
            a = [float(i)*100 for i in re.findall('\d+\.?d*',x)]
        if x[-1] == '年':
            a = [i/12 for i in a]
        return a
    except:
        return x

gongzi(y)

salary = job_info['工资'].apply(gongzi)

job_info['最低工资'] = salary.str[0]

job_info['最高工资'] = salary.str[1]

job_info['平均工资'] = job_info[['最低工资','最高工资']].mean(axis=1)

#公司类型
job_info['公司类型'].value_counts()
job_info['公司类型'].str[1]

