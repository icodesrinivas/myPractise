

def findSum(A, N):
    min_n = A[0]
    max_n = A[0]

    for item in A:
        if item < min_n: min_n = item
        if item > max_n: max_n = item

    return min_n + max_n

print(findSum([1, 3, 4, 1], 4))