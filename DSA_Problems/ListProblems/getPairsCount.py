"""
Count pairs with given sum

Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation:
arr[0] + arr[1] = 1 + 5 = 6
and arr[1] + arr[3] = 5 + 1 = 6.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""

def getPairsCount(arr, n, k):

    d = {}
    count = 0
    for item in arr:
        if item >= k: continue

        if k - item in d:
            count += d[k - item]

        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    return count

print(getPairsCount([2, 2, 2, 2], 4, 6))





