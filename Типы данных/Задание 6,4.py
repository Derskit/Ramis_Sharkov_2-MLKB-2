z = str(input())         # z текст
x = ''                   # x результат
n = z.find('(')          # n начало скобок
                         # k конец скобок
while n != -1:
    k = z.find(')',n)
    if k!= -1:
        x += z[n +1:k]
    else:
        break
    n = z.find("(",k)
print(x)