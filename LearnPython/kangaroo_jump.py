def kangaroo(x1, v1, x2, v2):
    if (x2 > x1 and v2 >= v1) or (x1 > x2 and v1 >= v2):
        return 'NO'
    else:
        total_jumps = abs(x2 - x1) / abs(v1 - v2)

        if (total_jumps % 1) == 0:

            if (v1 * total_jumps) + x1 == (v2 * total_jumps) + x2:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'

print(kangaroo(21, 6, 47, 3))