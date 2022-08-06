"""
Find duplicates in an array

Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: -1
Explanation: N=4 and all elements from 0
to (N-1 = 3) are present in the given
array. Therefore output is -1.
"""
import collections
from collections import Counter
def duplicates(arr, n):
    arr = Counter(arr)
    result = []
    for item in arr:
        if arr[item] > 1: result.append(item)
    return result


def duplicates2(arr, n):
    for i in range(0, n):
        index = arr[i] % n
        arr[index] += n

    print(arr)

print(duplicates2([2,13,1,2,8], 5))

