def reg():
    f = str(input('Введите фамилию:'))
    i = str(input('Введите имя:'))
    o = str(input('Введите отчество:'))
    v = int(input('Введите возвраст:'))
    v1 = 2023 - v
    v0 = str(v1)
    print(f,i,o,v0,'г.р. зарегистрирован')
reg()
