import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 3000)
y = np.random.normal(3, 4, 3000)
plt.scatter(x, y, alpha=0.15,c = 'r' ,s = 10, marker='>')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('точки')

plt.show()