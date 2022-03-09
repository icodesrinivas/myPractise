def permutationEquation(p):
    return [1 + p.index(1 + p.index(index)) for index in range(1, len(p)+1)]

# l = [3,4,2,1]
# print(l.index(4))

def p(x):
    global arr
    return arr[x-1]

arr = [5,2,1,3,4]
brr = map(lambda x:p(p(x)), arr)
for i in arr:
    print(arr.index(i) + 1)