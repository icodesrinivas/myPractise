def kaprekarNumbers(p, q):
    result = []
    for i in range(p, q + 1):
        sq = str(i ** 2)

        if int(sq) == 1:
            result.append(str(i))
        if len(sq) > 1:
            mid = len(sq) // 2
            if int(sq[:mid]) + int(sq[mid:]) == i:
                result.append(str(i))

    print(' '.join(result))

kaprekarNumbers(1,100)