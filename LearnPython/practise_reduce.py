from functools import reduce

lis = [1, 3, 5, 6, 2, 5]

print(reduce(lambda a,b: a if a > b else b, lis))

