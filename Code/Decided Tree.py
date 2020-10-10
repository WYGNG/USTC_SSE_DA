import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

data_tr = pd.read_csv('iris_tr.csv')
data_te = pd.read_csv('iris_te.csv')
labels = data_te['class']

#data_tr.iloc[:, 2:3]

Dct = DecisionTreeClassifier()
Dct.fit(data_tr.iloc[:, :-1], data_tr.iloc[:, -1])
pre = Dct.predict(data_te.iloc[:, :-1])
#pre == labels
confusion_matrix(labels,pre)
report=classification_report(labels,pre)
print(report)
