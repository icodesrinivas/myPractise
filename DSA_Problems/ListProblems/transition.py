"""
Given a sorted array containing only 0s and 1s, find the transition point.


Example 1:

Input:
N = 5
arr[] = {0,0,0,1,1}
Output: 3
Explanation: index 3 is the transition
point where 1 begins.

Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
"""
def transition(arr, n):

    start = 0
    end = n-1

    while start <= end:
        mid = start + (end - start) // 2
        if mid + 1 > n - 1: return -1

        if arr[mid] == 0 and arr[mid+1] == 1: return mid+1
        if arr[mid] == 1 and arr[mid-1] == 0: return mid

        if arr[mid] == 1 and arr[mid-1] == 1: end = mid-1
        if arr[mid] == 0 and arr[mid+1] == 0: start = mid+1

    return -1

print(transition([0,0,0,0,0,0,0,1], 8))

