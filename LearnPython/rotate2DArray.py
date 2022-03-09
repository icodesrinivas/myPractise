
# def shiftRight(arr, m, n):

lis = [1,2,3,4]
print([i for i in lis])

import numpy as np

def rotate2DArray(matrix):
    n = len(matrix)
    result = []
    for row_index in range(len(matrix)-1, -1, -1):
        for item_index in range(len(matrix[row_index])):
            if len(result) < len(matrix[row_index]):
                result.append([matrix[row_index][item_index]])
            else:
                result[item_index].append(matrix[row_index][item_index])


    print(np.array(result))

def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

myList1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
myList2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print(rotate_matrix(myList1))
rotate2DArray(myList2)