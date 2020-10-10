import pandas as pd
data = pd.read_csv('../data/message80W1.csv',header= None, index_col=0)
data.columns = ['label','message']
data.shape

data['label'].value_counts()
n = 1000
a = data[data['label']==0].sample(n,random_state=123)
b = data[data['label']==1].sample(n,random_state=456)
data_new = pd.concat([a,b],axis=0)
#去重
data_dup = data_new['message'].drop_duplicates()
#删除x
import re
data_qumin = data_dup.apply(lambda x:re.sub('x','',x))
#分词
import jieba
data_cut =data_qumin.apply(lambda x: jieba.lcut(x))
jieba.lcut('女人节促销活动')
jieba.lcut('唯品会打折')
jieba.load_userdict('../data/newdic1.txt')
jieba.lcut('女人节促销活动')
jieba.lcut('唯品会打折')
data_cut =data_qumin.apply(lambda x: jieba.lcut(x))

#去停用词
stopWords = pd.read_csv('stopword.txt',sep='yiersan',header=None)
data_stop = data_cut.apply(lambda x:[i for i in x if i not in stopWords])
stopWords_new = [' ','：','“','”','，','-','【','!']+list(stopWords.iloc[:,0])
data_stop = data_cut.apply(lambda x:[i for i in x if i not in stopWords_new])
data_stop = pd.concat([data_stop, data_new.loc[data_stop.index, 'label']],axis=1)

#绘制词云图
from wordcloud import WordCloud
import matplotlib.pyplot as plt
word_fre = {}
#data_stop.loc[data_stop['label']==1,'message']
for i in data_stop.loc[data_stop['label']==0,'message']: #遍历垃圾短信
    for j in i:#遍历短信中的词语
        if j not in word_fre.keys():
            word_fre[j] = 1
        else:
            word_fre[j]+=1
word_fre.items()
word_fre_order = sorted(word_fre.items(),key=lambda x:x[1],reverse=True)
mask = plt.imread('duihuakuang.jpg')
wc = WordCloud(mask=mask,background_color='white',font_path='C:\Windows\Fonts\simhei.ttf')
wc.fit_words(word_fre)
plt.imshow(wc)

#构建识别垃圾短信的模型
from sklearn.model_selection import train_test_split
data_tr, data_te, label_tr,label_te = train_test_split(data_stop['message'],data_stop['label'],test_size=0.2,random_state=123)
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
data_tr[370634]
type(' '.join(data_tr[370634]))
data_tr1 = data_tr.apply(lambda x: ' '.join(x))
cv = CountVectorizer()
data_tr_f = cv.fit_transform(data_tr1) #训练集词频矩阵
X_tr = TfidfTransformer().fit_transform(data_tr_f.toarray()).toarray()#训练集tf-idf矩阵
data_te1 = data_te.apply(lambda x: ' '.join(x))
data_te_f = CountVectorizer(vocabulary=cv.vocabulary_).fit_transform(data_te1)#测试集词频矩阵
X_te = TfidfTransformer().fit_transform(data_te_f.toarray()).toarray()#测试集tf-idf矩阵

#贝叶斯分类器
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()#调用模型
model.fit(X_tr,label_tr)#训练模型
pre = model.predict(X_te)
from sklearn.metrics import confusion_matrix, classification_report
confusion_matrix(label_te,pre)
report = classification_report(label_te, pre)
print(report)

#举例
texts=["orange banana apple grape","banana apple apple","grape", 'orange apple']
cv1 = CountVectorizer()
cv1_fit=cv1.fit_transform(texts)
print(cv1)
print(cv1.vocabulary_)
print(cv1_fit)
print(cv1_fit.toarray())
tests=["banana orange peach","pear apple apple"]
cv2 = CountVectorizer(vocabulary=cv1.vocabulary_)
cv2_fit=cv2.fit_transform(tests)
print(cv2)
print(cv2.vocabulary_)
print(cv2_fit)
print(cv2_fit.toarray())
