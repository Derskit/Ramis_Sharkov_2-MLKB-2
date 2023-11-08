a = input()
b = input()
c = input()
a1 = a.split()
b1 = b.split()
c1 = c.split()
z = a1 + b1 + c1
c = []
n = 0
for i in z:
    if z.count(i) == 3 not in c:
        c.append(i)
        v = {}.fromkeys(c)
        c=list(v.keys())
        c.sort()
        n = 1
if n == 1:
    print(' '.join(c))
else:
    print('Все три задачи никто не решил')