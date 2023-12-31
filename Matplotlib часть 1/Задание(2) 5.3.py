import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(16, 2, 1000)
plt.grid()
plt.ylabel('кол-во школьников')
plt.xlabel('секунды')
plt.title('100 метровка')

z = plt.hist(data, color = 'r',alpha = 0.5)

x = np.delete(z[1],-1)
y = z[0]
print(f'минимальное время забега составляет {min(x)} секунд')
print(f'максимальное время забега составляет {max(x)} секунд')

print(f'Большинсто учениковв ({int(max(y))} человек) пробежало дистанцию за {x[np.where(y == (max(y)))[0][0]]} секунд')
print(f'Меньшинсто учениковв ({int(min(y))} человек) пробежало дистанцию за {x[np.where(y == (min(y)))[0][0]]} секунд')
plt.show()

