import numpy as np
n = 0
for i in range(0,1000):
    arr = np.random.randint(1, 10, size=100)
    a = arr[arr > 7]
    if len(a) == 20:
        n += 1
print(n/10,'%')
