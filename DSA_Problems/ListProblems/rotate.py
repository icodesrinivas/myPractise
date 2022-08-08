
"""
Cyclically rotate an array by one

Given an array, rotate the array by one position in clock-wise direction.


Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def rotate(arr, n):

    temp = arr[-1]
    for i in range(n-1, -1, -1):
        if i==0: arr[i] = temp
        else: arr[i] = arr[i-1]
    return arr

print(rotate([9, 8, 7, 6, 4, 2, 1, 3], 8))