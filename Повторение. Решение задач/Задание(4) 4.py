import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

dt = pd.read_csv('titanic.csv')
print(dt.isna().sum())
dt =dt.dropna(axis=0)
print(dt.isna().sum())
print(dt.describe(include= ['object']))
dt = dt.drop(['Name', 'Gender','Ticket','Cabin', 'Embarked'],axis=1)
data = (dt - dt.mean(axis=0))/dt.std(axis=0)
X = data.drop('Survived',axis=1)
Y = dt['Survived']
X_tr, X_test, Y_tr, Y_test = train_test_split(X,Y, test_size= 0.3, random_state= 42)

log = LogisticRegression()
log.fit(X_tr,Y_tr)
Y_pr_log = log.predict(X_test)

KNN = KNeighborsClassifier()
KNN.fit(X_tr,Y_tr)
Y_pr_KNN = KNN.predict(X_test)

f1_log = f1_score(Y_test, Y_pr_log)
f1_KNN = f1_score(Y_test, Y_pr_KNN)
print('F1 мера для LogisticRegression: ', f1_log)
print('F1 мера для KNeighborsClassifier: ', f1_KNN)
if f1_log > f1_KNN:
    print('LogisticRegression справляется лучше KNeighborsClassifier')
else:
    print('KNeighborsClassifier справляется лучше LogisticRegression')
