# from itertools import combinations_with_replacement, combinations
#
# print(combinations(4, 2))
# n = 4
# a = 10
# b = 100
# print([a] * 2 + [b])
# perm = combinations_with_replacement([10,10,10,100], 4)
# [print(sum(p)) for p in perm]

# for i in range(4):


from itertools import combinations

def stones(n, a, b):
    # Write your code here
    result = []
    i = 1
    j = n-2
    while i < n-1:
        end_number = (i * a) + (j * b)
        if end_number not in result:
            result.append((i * a) + (j * b))
        i += 1
        j -= 1

    start_number = a * (n-1)
    last_number = b * (n-1)
    if start_number not in result:
        result.insert(0, (a * (n-1)))
    if last_number not in result:
        result.append((b * (n-1)))
    print(sorted(result))
    return sorted(result)
stones(73, 25, 25)
