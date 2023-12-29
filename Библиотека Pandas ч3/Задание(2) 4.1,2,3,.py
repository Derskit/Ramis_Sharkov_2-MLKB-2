import pandas as pd
path="Customers.csv"
data = pd.read_csv(path,delimiter=';')
print('До изменнений')
print(data)
df = data.isna().sum()
print(df)
df2 = (data.dropna())
print('После проверки и очистки пустых строк')
print(df2)
print(df2.isna().sum())
print('Средний годовой доход')
z = df2.groupby('Profession')['Income'].agg(['mean'])
print(z)