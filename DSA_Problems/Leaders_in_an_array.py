
def leaders(A, N):

    result = []
    max = None
    for i in range(N-1, -1, -1):
        if not max or A[i] > max:
            max = A[i]
            result.append(A[i])


    return result[::-1]

print(leaders([63, 70, 80, 33, 33, 47, 20], 7))
