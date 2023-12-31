import matplotlib.pyplot as plt
import numpy as np

def giperbola(x):
    return 1/x
x = np.linspace(1, 15, 100)
y = giperbola(x)
plt.plot(x,y, dashes=[5, 5], color = 'g',alpha = 0.5)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Вот такая моя функция')
plt.show()