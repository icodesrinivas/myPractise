# Return product of 3 elements such that it returns highest product from the list

def highest_product(A):

    A.sort()

    if len(A) < 2:
        return 'Input should at least have 3 elements'

    if A[0] < 0 and A[1] < 0:
        return A[0] * A[1] * A[-1]
    else:
        return A[-1] * A[-2] * A[-3]

print(highest_product([-5,-2,-1,0,0,1,1,5]))
