n = int(input())
a = list(range(2,n +1))
m = 2
q = 0
c = 1
print(a)
while q != 1:
    if m < n:
        for i in a:
            if i % m == 0 and i != m:
                a.pop(a.index(i))
        m += 1
    else:
        break
print(a)