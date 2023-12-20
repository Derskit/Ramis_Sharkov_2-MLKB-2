import numpy as np
arr = np.random.randint(1, 10, size=100)
print(arr)
a = arr[arr > 7]
print(len(a),'%')
