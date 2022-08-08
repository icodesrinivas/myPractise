"""
Minimum distance between two numbers

You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

Example 1:

Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def minDist(arr, n, x, y):
    dist = float('inf')
    x_index = None
    y_index = None
    for i in range(n):
        if arr[i] == x: x_index = i
        if arr[i] == y: y_index = i

        if x_index is not None and y_index is not None:
            print('abs(x_index - y_index)', abs(x_index - y_index))
            dist = min(dist, abs(x_index - y_index))

        print('x_index',x_index,'y_index',y_index)

    if dist != float('inf'): return dist

    return -1

arr = '96 82 48 76 34 19 7 80 36 57 77 34 19 35 5 57 16 66 42 62 89 19 60 19 25 16 20 51 77 75 12 73 8 11 100 93 81 58 72 17 14 48 2 33 82 6 41 49 72 34 10 12 53 21 30 77 36 49 79 13 75 42'.split()
arr = list(map(int, arr))


print(minDist([1,2], 2, 1, 2))
