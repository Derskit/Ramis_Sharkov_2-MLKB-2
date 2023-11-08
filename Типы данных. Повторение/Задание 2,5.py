z = input()
x = ''
b = True
for i in range(len(z)):
    if z[i].isalpha():
        if b:
            x += z[i].upper()
            b = False
        else:
            x += z [i].lower()
    else:
        x += z[i]
        if z[i] in ['.','?','!']:
            b = True
print(x)