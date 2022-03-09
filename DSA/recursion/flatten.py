
print(type(1) == list)

def flatten(arr):
    print('arr', arr)
    if len(arr) == 0:
        return []
    else:
        if type(arr[0]) == list:
            return flatten(arr[0]) + flatten(arr[1:])
        else:
            return [arr[0]] + flatten(arr[1:])

print(flatten([1, [2, [3, 4], [[5]]]]))
