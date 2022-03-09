
def shell_sort(arr):

    gap = len(arr) // 2
    size = len(arr)

    while gap > 0:

        pos = 0

        while pos < gap:

            for i in range(pos + gap, size, gap):
                if arr[i] < arr[i-gap]:
                    arr[i], arr[i-gap] = arr[i-gap], arr[i]

            pos += 1

        gap -= 1

    return arr

print(shell_sort([5,9,3,1,2,8,4,7,6]))