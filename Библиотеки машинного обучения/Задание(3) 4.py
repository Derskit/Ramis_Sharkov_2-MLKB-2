from sklearn.model_selection import train_test_split # функция для разделения данных на тестовый и обучающий набор
from sklearn.linear_model import LinearRegression # класс линейной регрессии
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # один признак
y = 4 + 3 * X + np.random.randn(100, 1)  # целевая переменная с небольшим шумом
X_tr, X_test, y_tr, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_tr,y_tr)

y_pr = model.predict(X_test)
print(y_pr)

plt.figure(figsize=(8,5))
plt.scatter(X_tr,y_tr, color = 'red', label = 'Тренировочные данные')
plt.scatter(X_test,y_test, color = 'green', label = 'Тестовые данные',alpha=0.7)
plt.plot(X_test,y_pr, color = 'blue',label = "Линейная регрессия")
plt.xlabel('Признак')
plt.ylabel('Целевая переменная')
plt.title('Линейнная регрессия (обучающий и тестовый наборы)')
plt.grid(True)
plt.legend()
plt.show()