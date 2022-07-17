

# def allPairs(self, A, B, N, M, X):

def allPairs(A, B, N, M, X):
    A.sort()
    B.sort()

    pair_list = []

    for i in range(N):

        target = X - A[i]

        if target in B:
            if (A[i], target) not in pair_list:
                pair_list.append((A[i], target))

    return pair_list

print(allPairs([1, 2, 4, 5, 7], [5, 6, 3, 4, 8], 5, 5, 9))