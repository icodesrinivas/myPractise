
def selection_sort(arr):

    for i in range(len(arr)-1,0,-1):
        print(arr)
        max_index = i
        for j in range(i):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr

print(selection_sort([5,9,3,1,2,8,4,7,6]))



