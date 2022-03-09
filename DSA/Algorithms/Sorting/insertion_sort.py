
def insertion_sort(arr):

    for i in range(1, len(arr)):

        anchor = arr[i]
        j = i

        while anchor <= arr[j-1] and j >= 1:
            if anchor < arr[j-1]:
                arr[j] = arr[j-1]
            j -= 1

        arr[j] = anchor

    return arr

print(insertion_sort([5,9,3,1,2,8,4,7,6]))