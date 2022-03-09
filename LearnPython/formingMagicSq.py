def formingMagicSquare(s):
    diag_max = max([sum([s[i][i] for i in range(len(s))]), sum([s[i][-(i + 1)] for i in range(len(s))])])
    diag_min = min([sum([s[i][i] for i in range(len(s))]), sum([s[i][-(i + 1)] for i in range(len(s))])])
    print(diag_max)
    print(diag_min)
    cost_max = sum([abs(diag_max - sum(i)) for i in s])
    cost_min = sum([abs(diag_min - sum(i)) for i in s])
    print('cost_max',cost_max)
    print('cost_min',cost_min)

lis = [[4,5,8], [2,4,1], [1,9,7]]
lis2 = [[4,9,2], [3,5,7], [8,1,5]]
formingMagicSquare(lis2)