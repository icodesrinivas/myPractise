def beautifulTriplets(d, arr):
    if len(arr) > 2:
        count = 0
        for k in range(len(arr)-1, 1, -1):
            j = arr[k]-d
            i = arr[k]-(2*d)
            j_count = arr.count(j)
            i_count = arr.count(i)
            if j in arr[:k] and i in arr[:k]:
                count = count + (j_count * i_count)
    print(count)
beautifulTriplets(3, [1,6,7,7,8,10,12,13,14,19])