"""
Minimize the sum of product

You are given two arrays, A and B, of equal size N. The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] +…+ A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.

Input:
N = 3
A[] = {3, 1, 1}
B[] = {6, 5, 4}
Output:
23
Explanation:
1*6+1*5+3*4 = 6+5+12
= 23 is the minimum sum

Input:
N = 5
A[] = {6, 1, 9, 5, 4}
B[] = {3, 4, 8, 2, 4}
Output:
80
Explanation:
2*9+3*6+4*5+4*4+8*1
=18+18+20+16+8
= 80 is the minimum sum
"""


def minValue(a, b, n):
    # Your code goes here
    a = list(reversed(sorted(a)))
    b = list(sorted(b))
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]

    return sum

print(minValue([3, 1, 1], [6, 5, 4], 3))