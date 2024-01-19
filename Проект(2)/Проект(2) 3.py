import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Housing.csv')
plt.figure(figsize=(15, 9))
plt.subplot(2, 2, 1)
for g in df['guestroom'].unique():
    subset = df[df['guestroom'] == g]
    plt.scatter(subset['price'], subset['area'], label=g,alpha=0.5,marker='*')
plt.legend()
plt.grid()
plt.title('Квартиры по наличию гостевых комнат')
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.subplot(2, 2, 2)
for b in df['basement'].unique():
    subset = df[df['basement'] == b]
    plt.scatter(subset['price'], subset['area'], label=b,alpha=0.5,marker='.')
plt.legend()
plt.grid()
plt.title('Квартиры по наличию подвала')
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.subplot(2,2,3)
for h in df['hotwaterheating'].unique():
    subset = df[df['hotwaterheating'] == h]
    plt.scatter(subset['price'], subset['area'], label=h,alpha=0.5,marker='+')
plt.legend()
plt.grid()
plt.title('Квартиры по наличию горячей воды')
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.subplot(2,2,4)
for p in df['prefarea'].unique():
    subset = df[df['prefarea'] == p]
    plt.scatter(subset['price'], subset['area'], label=p,alpha=0.5,marker='x')
plt.legend()
plt.grid()
plt.title('Квартиры по наличию предбанника')
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.show()