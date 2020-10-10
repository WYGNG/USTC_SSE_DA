import pandas as pd
data = pd.read_csv('../data/message80w1.csv', header= None, index_col=0)
data.columns = ['label','message']
data.shape

data['label'].value_counts()

n=1000
a=data[data['label']==0].sample(n,random_state=123)
b=data[data['label']==0].sample(n,random_state=456)

data_new =pd.concat([a,b],axis=0)

#去重
data_dup = data_new['message'].drop_duplicates()

#删除
import re
data_qumin = data_dup.apply(lambda x:re.sub('x','',x))

import jieba
data_cut = data_qumin.apply(lambda x: jieba.lcut(x))
jieba.lcut('女人节促销活动')
jieba.lcut('唯品会打折')
#jieba.load_userdict('newdic1.txt')

jieba.lcut('女人节促销活动')
jieba.lcut('唯品会打折')
data_cut = data_qumin.apply(lambda x: jieba.lcut(x))

#去停用词
stopWords = pd.read_csv('../data/stopword.txt', sep='yiersan',header=None)
data_stop = data_cut.apply(lambda x:[i for i in x if i not in stopWords])

stopWords_new = ['','：','“','”','，','-','【','','！']+list(stopWords.iloc[:,0])
data_stop = data_cut.apply(lambda x:[i for i in x if i not in stopWords])
data_stop = pd.concat([data_stop, data_new.loc[data_stop.index, 'label']],axis=0)
#绘制词云图

from wordcloud import WordCloud
import matplotlib.pyplot as plt
word_fre = {}
#data_stop.loc[data_stop['label']==1,'message']

for i in data_stop.loc[data_stop['label']==0,'message']:
    for j in i:
        if j not in word_fre.keys():
            word_fre[j] = 1
        else:
            word_fre[j] += 1

word_fre.items()
word_fre_order = sorted(word_fre.items(),key=lambda  x:x[1], reverse=True)







mask = plt.imread('duihuakuang,jpg')
wc = WordCloud(mask=mask,background_color='white')
wc.fit_words(word_fre)

plt.imshow(wc)


from sklearn.model_selection import train_test_split


train_test_split()

