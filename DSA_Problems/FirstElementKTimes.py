"""
First element to occur k times

Given an array of N integers. Find the first element that occurs atleast K number of times.

Input :
N = 7, K = 2
A[] = {1, 7, 4, 3, 4, 8, 7}
Output :
4
Explanation:
Both 7 and 4 occur 2 times.
But 4 is first that occurs 2 times.
"""


def firstElementKTime(a, n, k):
    # code here
    result = {}

    for i in range(len(a)):

        if a[i] not in result:
            result[a[i]] = 1
        else:
            result[a[i]] += 1

        if result[a[i]] == k:
            return a[i]

    return -1