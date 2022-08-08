"""
Find triplets with zero sum

Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero.

Example 1:

Input: n = 5, arr[] = {0, -1, 2, -3, 1}
Output: 1
Explanation: 0, -1 and 1 forms a triplet
with sum equal to 0.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)
"""
def findTriplets(arr, n):

    arr.sort()

    for i in range(0, n- 1):
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r] == 0): return 1
            elif (x + arr[l] + arr[r] < 0): l += 1
            else: r -= 1

    return 0