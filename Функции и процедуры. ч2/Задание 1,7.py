n = 0
print('Введите первый список:')
while n != 1:
    a = []
    a0 = 0
    while a0 != '':
        a0 = input()
        if a0 != '':
            a.append(a0)

    n += 1
n = 0
print('Введите второй список:')
while n != 1:
    b = []
    b0 = 0
    while b0 != '':
        b0 = input()
        if b0 != '':
            b.append(b0)
    n += 1
r1 = list(map(int,a))
r2 = list(map(int,b))
c = list(map(lambda x, y: x + y,r1,r2))
print(c)