

def largestNum(n, s):

    if n == 1 and s < 10:
        return int(str(s)[0])

    if s / n > 9:
        return -1

    nines = s // 9

    if nines == n:
        return int("".join(map(str, [9]*nines)))

    rem = s % 9
    number = [9] * nines + [rem] + ([0] * (n - (nines + 1)))
    return int("".join(map(str, number)))

print(largestNum(3, 9))