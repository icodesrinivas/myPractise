
# Swap and maximize
# Given an array, consider array as a circular array and the task is to
# find max sum of abs diff between consecutive ele with rearrangements

def maxSum(arr, n):

    arr.sort()

    min_ele = 0
    max_ele = n-1

    ans = 0

    while min_ele < max_ele:

        ans += abs(arr[min_ele] - arr[max_ele])

        if min_ele <= (n - 1) - max_ele:
            min_ele += 1
        else:
            max_ele -= 1

    ans += (arr[max_ele] - arr[0])

    return ans



print(maxSum([4, 2, 1, 8], 4))