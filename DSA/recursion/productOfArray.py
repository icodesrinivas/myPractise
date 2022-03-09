
l = [1,2,3,4]
# for item in range(len(l)-1, -1, -1):
#     print(l[item])

def productOfArray(arr):
    if len(arr) == 1:
        return arr.pop()
    else:
        return arr.pop() * productOfArray(arr)
print(productOfArray(l))