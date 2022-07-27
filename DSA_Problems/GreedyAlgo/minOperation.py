"""
Minimum Operations

Given a number N. Find the minimum number of operations required to reach N starting from 0. You have 2 operations available:

Double the number
Add one to the number

Input:
N = 8
Output: 4
Explanation: 0 + 1 = 1, 1 + 1 = 2,
2 * 2 = 4, 4 * 2 = 8
"""

def minOperations(n):

    op = 0
    while n>0:
        if n <= 3:
            if n == 3: op += 3
            if n == 2: op += 2
            if n == 1: op += 1
            break

        if n%2 == 1:
            n -= 1
            op += 1
        else:
            n //= 2
            op += 1

    return op

print(minOperations(7))