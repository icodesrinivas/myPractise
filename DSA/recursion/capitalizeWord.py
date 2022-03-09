def capitalizeWords(arr):
    print(arr)
    if len(arr) == 1:
        return [arr[0].upper()]
    else:
        popped_arr = arr.pop()
        return + + [popped_arr.upper()]
