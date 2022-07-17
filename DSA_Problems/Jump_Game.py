
def canReach(A, N):
    n = N - 1
    for i in range(n - 1, -1, -1):
        if A[i] + i >= n:
            n = i

    if n == 0:
        return 1
    else:
        return 0




print(canReach([1,2,0,3,0,0], 6))

# lis = '5 9 3 2 1 0 2 3 3 1 0 0'.split(' ')
# lis = list(map(int, lis))
# print(canReach(lis, len(lis)))





