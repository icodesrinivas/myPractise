arr = [12,13,14,11,10,10,22,-23, 14,16,-28, -28]
arr1 = []

def findMaxProduct(arr):
    if len(arr) in [0,1]:
        return 'More than 1 elements required in the array.'

    if any(map(lambda x: type(x) != int, arr)):
        return 'List must contain only the integers'

    prev_max = arr[0]
    curr_max = arr[1]

    for i in range(2, len(arr)):
        if arr[i] > curr_max:
            prev_max = curr_max
            curr_max = arr[i]
        elif arr[i] > prev_max:
            prev_max = arr[i]
        else:
            continue
    print(prev_max, curr_max)
    return prev_max * curr_max

print(findMaxProduct(arr1))
