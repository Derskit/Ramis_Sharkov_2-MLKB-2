from functools import reduce
n = 0
print('Введите список:')
while n != 1:
    a = []
    a0 = 0
    while a0 != '':
        a0 = input()
        if a0 != '':
            a.append(a0)

    n += 1
r = list(map(int,a))
x = reduce(max,r)
print(x)