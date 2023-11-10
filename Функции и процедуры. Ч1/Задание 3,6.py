def maximum():
    n = 0
    while n != 1:
        z = int(input('Введите количество вводимых числ от 2 до 3:'))
        if 1 < z < 4:
            n += 1
    a = input('Введите первое число:')
    b = input('Введите второе число:')
    if z == 3:
        c = input('Введите третье число:')
        if (a < b) and (b > c):
            print(b)
        elif (a < c) and (c > b):
            print(c)
        else:
            print(a)
    else:
        if a < b:
            print(b)
        else:
            print(a)
maximum()