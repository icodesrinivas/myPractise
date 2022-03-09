def myPageCount(n, p):
    count = 0
    if p > n//2:
        if n % 2 == 0:
            for i in range(n, n//2, -2):
                if p < i:
                    count += 1
        else:
            for i in range(n, n//2, -2):
                if p < i - 1:
                    count += 1
    else:
        for i in range(0, n // 2, 2):
            if p > i + 1:
                count += 1

    return count



# Best Solution
def pageCount(n, p):
    return min(p//2, n//2 - p//2)
print(pageCount(6,4))