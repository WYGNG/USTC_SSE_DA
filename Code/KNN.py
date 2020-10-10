import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report #混淆矩阵,即统计中的两类错误

data_tr = pd.read_csv('iris_tr.csv')
data_te = pd.read_csv('iris_te.csv')
labels = data_te['class']

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(data_tr.iloc[:, :-1], data_tr.iloc[:, -1])
pre = knn.predict(data_te.iloc[:, :-1])
pre == labels

confusion_matrix(labels,pre)#3*3矩阵，因为有3类标签
report = classification_report(labels,pre)#分类报告,准确率，召回率，f1系数，实际个数，最后一行是评估参数均值和总个数
print(report)
