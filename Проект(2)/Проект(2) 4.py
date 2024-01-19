import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Housing.csv')
df0 = df[df['airconditioning'] == 'yes']
df1 = df[df['airconditioning'] == 'no']
plt.figure(figsize=(10,5))
l = ['yes','no']
plt.hist([df0['price'],df1['price']],bins=(len(df)//10),label=l, alpha = 0.8)
plt.legend()
plt.title('Дома с кондиционером и без')
plt.xlabel('Цена')
plt.ylabel('Количество домов')
plt.grid()
plt.show()
