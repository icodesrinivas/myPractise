"""
Subarray with given sum

Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving from left to right.

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.
"""


def subArraySum(arr, n, s):
    # Write your code here
    i = 0
    while i < n:

        arraySum = arr[i]

        if arraySum == s:
            return [i + 1, i + 1]

        j = i + 1
        while j < n:

            if arraySum < s:
                arraySum += arr[j]

                if arraySum == s:
                    return [i+1, j+1]
                j += 1
            else:
                break
        i += 1

    return [-1]



# print(subArraySum(l, 10, 15))

def subArraySum2(arr, n, s):
    if n == 1:
        if arr[0] == s:
            return [1, 1]
        elif arr[0] != s:
            return [-1]

    i = 0
    Sum = arr[0]
    for j in range(1, n):
        print('i', i)
        Sum = Sum + arr[j]
        while Sum > s and i < j:
            Sum = Sum - arr[i]
            i += 1
        if Sum == s:
            return [i + 1, j + 1]
        print('j', j)
    return [-1]

l = '11,2,13,4,15,6,17,8,19,10'.split(',')
l = list(map(int, l))

print(subArraySum2(l, 10, 21))