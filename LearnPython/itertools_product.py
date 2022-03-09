from itertools import product, permutations

l1 = list(map(int, '1 2'.split()))
l2 = list(map(int, '3 4'.split()))

print(*list(product(l1, l2)))
print(' '.join(list(map(str, list(product(l1, l2))))))
# print(' '.join(list(product(l1, l2))))

print(list(permutations([1,3,2])))

