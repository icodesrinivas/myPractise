"""
Third largest element

Given an array of distinct elements. Find the third largest element in it.

Suppose you have A[] = {1, 2, 3, 4, 5, 6, 7}, its output will be 5 because it is the 3 largest element in the array A.

Example 1:

Input:
N = 5
A[] = {2,4,1,3,5}
Output: 3

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def thirdLargest(a, n):

    if len(set(a)) < 3:
        return -1

    first = a[0]
    second = float('-inf')
    third = float('-inf')

    for i in range(1, n):

        if a[i] > first:
            third = second
            second = first
            first = a[i]
        elif a[i] > second:
            third = second
            second = a[i]
        elif a[i] > third:
            third = a[i]

    return third

a = '884 337 689 587 748 308 451 785 682 600 733 537 403 188 162 562 274 513 383 617 662 508 111 57 160'.split()
print(list(sorted(a)))
a = list(map(int, a))

print(thirdLargest(a, len(a)))

