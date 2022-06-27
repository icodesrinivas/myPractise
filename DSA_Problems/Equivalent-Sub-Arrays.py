

def countDistinctSubarray(arr, n):

    k = len(set(arr))

    distinct_ele = {}

    result = 0
    right = 0
    window = 0

    for left in range(n):

        while right < n and window < k:

            if arr[right] in distinct_ele.keys():
                distinct_ele[arr[right]] += 1
            else:
                distinct_ele[arr[right]] = 1

            if distinct_ele[arr[right]] == 1:
                window += 1

            right += 1

        if window == k:
            result += (n - right + 1)

        distinct_ele[arr[left]] -= 1

        if distinct_ele[arr[left]] == 0:
            window -= 1

    return result

lis = '2 2 1 10 6 1 7 2 5 1 8 5 3 1 2 9 2 10 7 6 5 2'.split(' ')
lis = list(map(int, lis))

print(countDistinctSubarray(lis, 22))


