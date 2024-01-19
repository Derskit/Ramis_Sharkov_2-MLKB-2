import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Housing.csv')
plt.figure(figsize=(10,5))
for parking in df['parking'].unique():
    subset = df[df['parking'] == parking]
    plt.scatter(subset['price'], subset['area'], label=parking, alpha= 0.5, marker='*')
plt.legend()
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.title('Статистика по квартирам,их площади и количеству парковочных мест')
plt.show()
