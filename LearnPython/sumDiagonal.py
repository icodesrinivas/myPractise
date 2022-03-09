import numpy as np
def sumDiagonal(a):
    diagonal_sum = 0
    for row_index in range(len(a)):
        diagonal_sum += a[row_index][row_index]
    return diagonal_sum

myList = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(sumDiagonal(myList))
