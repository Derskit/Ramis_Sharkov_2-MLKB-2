import pandas as pd
data = pd.read_csv('Housing.csv')
print(data)
df = data[data['price']==data['price'].min()]
print('1) Количество спален в самом дешёвом доме',df['bedrooms'].min())
df2 = data[data['bedrooms'] <= data['bathrooms']]
print('2) Количество домов, в которых количество спален не больше количества ванных',len(df2))
df3 = data[data['guestroom'] == 'yes']
print('3) Самый дешёвый дом с гостевой комнатой стоит',df3['price'].min())
df4_1 = data[data['price'] <= 2000000]
df4_2 = data[data['price'] >= 5000000]
print('4.1) Процент домов до 2000000 с гостевой комнатой',(100/len(df4_1))*len(df4_1[df4_1['airconditioning'] == 'yes']),'%')
print('4.2) Процент домов от 5000000 с гостевой комнатой',(100/len(df4_2))*len(df4_2[df4_2['airconditioning'] == 'yes']),'%')
