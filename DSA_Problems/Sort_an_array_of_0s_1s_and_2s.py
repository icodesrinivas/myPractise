

def sort012(arr,n):

    zero = 0
    one = 0
    two = 0

    for i in range(n):
        if arr[i] == 0:
            zero += 1

        if arr[i] == 1:
            one += 1

        if arr[i] == 2:
            two += 1

    i = 0
    while zero > 0:
        arr[i] = 0
        i += 1
        zero -= 1

    while one > 0:
        arr[i] = 1
        i += 1
        one -= 1

    while two > 0:
        arr[i] = 2
        i += 1
        two -= 1

    return arr


def sort012Problem(arr,n):

    lo = 0
    mid = 0
    hi = n - 1

    while mid <= hi:

        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1

    return arr

print(sort012([0, 2, 1, 2, 0], 5))

