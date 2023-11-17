def maximum(l):
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return l[0]
    elif l[0] > l[1]:
        l.pop(1)
        return maximum(l)
    else:
        l.pop(0)
        return maximum(l)
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
print(r)
print(maximum(r))
