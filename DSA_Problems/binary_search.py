
def binarysearch(arr, n, k):
    # code here

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            return mid+1
        else:
            if k < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1



lis = list(map(int, '2 4 5 7 9 11 14 15 20 22 23 24 25 26 27 28 32 33 36 37 39 41 42 43 44 45 47 48 49 50 51 53 54 55 57 59 60 61 62 63 66 67 68 69 70 71 72 73 74 76 78 86 87 89 91 93 94 95 97 100'.split(' ')))
print('len',len(lis))
print(binarysearch(lis, len(lis), 60))