
arr = []
print(arr.append(list(map(int, '11 2 4'.split()))))
print(arr.append(list(map(int, '4 5 6'.split()))))

print(arr)


def diagonalDifference(arr):
    return abs(sum([arr[i - 1][-i] - arr[i - 1][i - 1] for i in range(1, len(arr) + 1)]))