
def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr)-1)

def quick_sort_helper(arr, first, last):

    if first < last:
        splitpoint = partition(arr, first, last)

        quick_sort_helper(arr, first, splitpoint-1)
        quick_sort_helper(arr, splitpoint+1, last)

    return arr


def partition(arr, first, last):

    pivot = arr[first]

    leftmark = first+1
    rightmark = last

    crossed = False

    while not crossed:

        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1

        while leftmark <= rightmark and arr[rightmark] >= pivot:
            rightmark -= 1

        if leftmark <= rightmark:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]
        else:
            crossed = True

    arr[first], arr[rightmark] = arr[rightmark], arr[first]

    return rightmark

i = 3
j = 7
arr = [11,9,29,7,2,15,28,1,10]
print(quick_sort(arr))

