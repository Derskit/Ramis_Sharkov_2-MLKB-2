import numpy as np
arr = np.random.randint(1, 10, size=100)
print(arr)
a = arr[arr > 7]
n = 100/len(arr)
print(n * len(a),'%')
