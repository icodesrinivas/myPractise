arr = []
for i in range(1, 101):
    arr.append(i)
arr.remove(54)
def findMissingNumber(arr, n):
    sum1 = (n * (n + 1)) / 2
    sum2 = sum(arr)
    return int(sum1 - sum2)

print(findMissingNumber(arr, 100))