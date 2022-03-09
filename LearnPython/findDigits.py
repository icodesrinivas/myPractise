def findDigits(n):
    m = n
    count = 0
    while m != 0:
        if (m % 10) != 0:
            if n % (m % 10) == 0:
                count += 1
        m = m // 10
    return count

print(findDigits(123))


