z = int(input())
x = 0
c = []
while x != z:
    x += 1
    c.append(input())
v = 0
b = 0
for i in c:
    v = c.count(i)
    if v > 1:
        b += 1
print(b)
