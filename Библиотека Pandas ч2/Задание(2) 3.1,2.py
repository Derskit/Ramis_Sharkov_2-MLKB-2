import pandas as pd
path="Customers.csv"
data = pd.read_csv(path,delimiter=';')
print('вся таблица')
print(data)

z1 = data[(data['Age'] > 30) & (data['Income']< 30000)]
z2 = data[(data['Profession'] == 'Lawyer')& (data['Work Experience']>5)]
print('возраст больше 30 и доход меньше 30000')
print(z1)
print('юристы и с опытом работы больше 5 лет')
print(z2)