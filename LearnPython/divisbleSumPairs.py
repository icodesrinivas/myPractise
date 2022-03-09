def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
    return result

print(divisibleSumPairs(5, 2, [5,9,10,7,4]))