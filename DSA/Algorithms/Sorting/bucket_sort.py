import math

def bubble_sort(arr):

    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bucket_sort(arr):
    total_buckets = [[] for _ in range(round(math.sqrt(len(arr))))]

    for i in arr:
        bucket_id = math.ceil(i * len(total_buckets)/max(arr))
        total_buckets[int(bucket_id) - 1].append(i)

    for l in total_buckets:
        l = bubble_sort(l)

    total_buckets = sum(total_buckets, [])
    print(total_buckets)


bucket_sort([1,2,4,91,95,93])
