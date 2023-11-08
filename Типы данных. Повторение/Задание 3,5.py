z = input()
x = input()
z = z.lower()
x = x.lower()
z = z.replace(' ','')
x = x.replace(' ','')
z1 = set(z)
x1 = set(x)
if z1 == x1:
    print('Строки являются анаграммами')
else:
    print('Строки не являются анаграммами')