z = str(input())
x = z.split()
x1 = []
for i in x:
    x1.append(int(i))
a = x1[-1]
x2 = []
x1.remove(a)
for q in x1:
    x2.append(q**a)
print(x2)