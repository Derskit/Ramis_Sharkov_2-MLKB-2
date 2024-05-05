from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

par = {'criterion': ['gini','entropy'],
       'max_depth': [1,2],
       'min_samples_split': [2,5,10]}
dt = DecisionTreeClassifier()
gridsearch = GridSearchCV(dt,par,cv=5)
gridsearch.fit(X_train,y_train)

best_par = gridsearch.best_params_
print(f'Наилучшие параметры:', best_par)
dt = DecisionTreeClassifier(criterion=best_par.get('criterion'),max_depth=best_par.get('max_depth'),min_samples_split=best_par.get('min_samples_split'))
dt.fit(X_train,y_train)
y_pr = dt.predict(X_test)
acc = accuracy_score(y_test,y_pr)
print(f'Оценка accuracy не тестовой выборке: {acc}')