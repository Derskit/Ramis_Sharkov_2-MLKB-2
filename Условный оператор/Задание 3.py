z = int(input())
x = int(input())
if z % 2 == 0:
    if x % 2 == 0:
        print("NO")
    else:
        print("YES")
elif z % 2 != 0:
    if x % 2 != 0:
        print("NO")
    else:
        print("YES")