import numpy as np

a_A = np.array([[1, 2],
                [4, 5],
                [7, 8]])

a_B = np.array([[1, 1, 0],
                [0, 1, 1],
                [1, 0, 1]])

b_A = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

b_B = np.array([[1, 1, 0],
                [0, 1, 1],
                [1, 0, 1]])

# a = np.matmul(a_A,a_B) перемножать нельзя, так как для выполнения матричного умножения первая матрица должна иметь такое же количество столбцов, сколько строк во второй матрице.
# print(a)
b = np.matmul(b_A, b_B)
print('b.')
print('A * B = ')
print(b)