def find(arr, n, x):
    first = None
    last = None

    for i in range(n):
        if not first and arr[i] == x:
            first = i
            last = i
        if arr[i] == x:
            last = max(last, i)

    if first:
        return [first, last]
    else:
        return [-1, -1]

print(find([1,1],2,2))