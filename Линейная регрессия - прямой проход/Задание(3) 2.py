import matplotlib.pyplot as plt
x = [1,3,7]
y = [2,6,14]
lr = 0.01
w0 = 0
w1 = 0
n = 1
loss = 0
while n == 1:
    for i in range(len(x)):
        prediction = w1 * x[i] + w0
        w1 += 2 * lr * x[i] * (y[i] - prediction)
        w0 += 2 * lr * (y[i] - prediction)
        loss = (y[i] - prediction) ** 2
    if loss == 0:
        print(w0,'= w0')
        print(w1,'= w1')
        n = 0
fig, ax = plt.subplots()
ax.grid()
plt.scatter(x, y, color = 'red')
plt.plot([0, 8], [w0, w1 * 8 + w0])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
