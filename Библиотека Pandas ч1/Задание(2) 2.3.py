import pandas as pd
data = {'множ-ль1':[1,2,3,4,5,6,7,8,9],'множ-ль2':[1,2,3,4,5,6,7,8,9],'произ-ие':[1,4,9,15,25,36,49,64,81]}
df = pd.DataFrame(data, index=['a','b','c','d','e','f','g','h','i'])
print(df)
df.to_csv('DataFrame1', encoding='utf-8')