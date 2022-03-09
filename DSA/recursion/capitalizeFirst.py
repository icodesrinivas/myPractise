
def capitalizeFirst(arr):
    if len(arr) == 0:
        return []
    else:
        popped_arr = arr.pop()
        return capitalizeFirst(arr) + [popped_arr.capitalize()]

print(capitalizeFirst(['car', 'bar', 'tar']))