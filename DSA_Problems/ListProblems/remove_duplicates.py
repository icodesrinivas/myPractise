
"""
Remove duplicate elements from sorted Array

Given a sorted array A[] of size N, delete all the duplicated elements from A[].Update the array such that if there are X distinct elements in it then the first X positions of the array should be filled with them in increasing order.

Note: Don't use set or HashMap to solve the problem.

Example 1:

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: 1
Explanation: After removing all the duplicates
only one instance of 2 will remain.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def remove_duplicates(A, N):
    i = 0
    k = N
    while i < k-1:
        if A[i] == A[i+1]:
            A.pop(i)
            k -= 1
        else: i += 1
    return len(A)

A = '1 3 4 5 6 12 13 17 19 22 23 25 27 28 28 35 36 37 39 43 46 48 54 59 62 63 65 68 68 70 70 72 79 82 83 92 92 93 95 96 96 100'.split()
A = list(map(int, A))
print(remove_duplicates(A, len(A)))