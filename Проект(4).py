import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

data = pd.read_csv('users_behavior.csv')
print(data.isna().sum())
X = data.drop('is_ultra', axis=1)
print(X)
Y = data['is_ultra']
X_tr, X_test, Y_tr, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

log = LogisticRegression(max_iter=150)
log.fit(X_tr,Y_tr)
Y_pr_log = log.predict(X_test)
acc_log = accuracy_score(Y_test, Y_pr_log)

accs = []
ks = list(range(1, 31))
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_tr, Y_tr)
    pr = clf.predict(X_test)
    acc = accuracy_score(Y_test, pr)
    accs.append(acc)

KNN = KNeighborsClassifier(n_neighbors=ks[accs.index(max(accs))])
KNN.fit(X_tr, Y_tr)
Y_pr_KNN = KNN.predict(X_test)
acc_KNN = accuracy_score(Y_test,Y_pr_KNN)

f1_log = f1_score(Y_test, Y_pr_log)
f1_KNN = f1_score(Y_test, Y_pr_KNN)
print('F1 мера для LogisticRegression: ', f1_log)
print('F1 мера для KNeighborsClassifier: ', f1_KNN)
if f1_log > f1_KNN:
    print('LogisticRegression справляется лучше KNeighborsClassifier')
else:
    print('KNeighborsClassifier справляется лучше LogisticRegression')
print("")
print(f'Оценка accuracy не тестовой выборке log: {acc_log}')
print(f'Оценка accuracy не тестовой выборке KNN: {acc_KNN}')

print(f'Самый оптимальный гиперпараметр k в KNeighborsClassifier: {ks[accs.index(max(accs))]}')

fig, ax = plt.subplots()
ax.plot(ks, accs)
ax.set(xlabel="k",
       ylabel="Accuracy",
       title="Performance of knn")
plt.grid()
plt.show()