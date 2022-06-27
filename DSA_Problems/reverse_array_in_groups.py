"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.

Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9
"""

lis = [1,2,3,4,5,6,1,2]

# for i in range(0, len(lis), 3):
#     print(i, i+3 if i+3<len(lis)-1 else len(lis))

# def reverseInGroups(arr, N, K):
#     # code here
#     result = []
#     for i in range(0, len(arr), K):
#
#         result.extend(reversed(arr[i:i+K]))
#
#     return result


def reverseInGroups(arr, N, K):
    # code here
    result = []
    for i in range(0, len(arr), K):

        lis = list(reversed(arr[i: i + K if i + K < N - 1 else N]))
        arr[i:i+K if i + K < N - 1 else N] = lis


    print('arr',arr)
    return result

print(reverseInGroups([1,2,3,4,5], 5, 3))

lis2 = [1,2,3,4,5]
lis2[0:2] = [22,33]
print(lis2)