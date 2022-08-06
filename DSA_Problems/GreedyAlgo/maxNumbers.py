
def maxNumbers(n, k, a):
    a = sorted(a)
    total = k
    count = 0
    i = 1
    j = 0
    while total > 0:
        if i != a[j]:
            total -= i
            if total >= 0: count += 1
            else: break
        else:
            if j < n-1: j += 1
        i += 1
    return count
print(maxNumbers(4, 25, [5, 6, 7, 8]))


