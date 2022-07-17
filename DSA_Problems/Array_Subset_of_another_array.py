

def isSubset( a1, a2, n, m):

    a1 = set(a1)

    result = all(map(lambda x: x in a1, a2))

    if result == True:
        return 'Yes'
    else:
        return 'No'

print(isSubset([1, 2, 3, 4, 5, 6], [1, 2, 9], 6, 3))