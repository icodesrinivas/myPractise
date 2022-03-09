
def merge_sort(arr):

    if len(arr) > 1:
        half = len(arr) // 2
        left = merge_sort(arr[:half])
        right = merge_sort(arr[half:])


        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1


        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    return arr

    # return arr

print(merge_sort([5,9,3,1,2,8,4,7,6]))


