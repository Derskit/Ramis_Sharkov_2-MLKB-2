p = int(input())
o = int(input())
b = min(o,p)
a = max(o,p)
if a % b == 0:
    x = b
else:
    z = a % b
    if b % z == 0:
        x = z
    else:
        z1 = b % z
        while z1 != 0 and z != 0:
            z = z % z1
            if z == 0:
                x = z1
                break
            z1 = z1 % z
            if z1 == 0:
                x = z
                break
print((a * b)/x)
