def cutTheSticks(arr):
    # Write your code here
    result = [len(arr)]

    while len(arr) > 0:
        arr = [y for y in list(map(lambda x: x - min(arr), arr)) if y != 0]
        if len(arr) > 0:
            result.append(len(arr))

    return result

print(cutTheSticks([5, 4, 4, 2, 2, 8]))