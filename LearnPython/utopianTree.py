def utopianTree(n):
    if n == 0:
        return 1
    else:
        if n%2 == 0:
            return utopianTree(n-1) + 1
        else:
            return utopianTree(n-1) * 2
    # print(pow(2, (n + 1) / 2 + 1) - 1 - (n % 2))

utopianTree(5)