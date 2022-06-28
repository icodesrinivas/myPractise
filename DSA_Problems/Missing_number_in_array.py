
def MissingNumber(array,n):

    array_total = sum(array)

    total = (n * (n + 1)) // 2

    return total - array_total

print(MissingNumber([6,1,2,8,3,4,7,10,5], 10))
