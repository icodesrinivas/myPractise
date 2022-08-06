"""
Largest Permutation

Given a permutation of first n natural numbers as an array and an integer k. Print the lexicographically largest permutation after at most k swaps.

Input:
n=5
k=3
arr[] = {4, 5, 2, 1, 3}
Output: 5 4 3 2 1
Explanation: Swap 1st and 2nd elements: 5 4 2 1 3
             Swap 3rd and 5th elements: 5 4 3 1 2
             Swap 4th and 5th elements: 5 4 3 2 1
"""

def KswapPermutation(arr, n, k):
    d = {arr[i]: i for i in range(n)}

    m = n
    for i in range(n):
        if arr[i] < m:
            temp = arr[i]
            arr[i] = m
            arr[d[m]] = temp
            d[temp], d[m] = d[m], d[temp]
            k -= 1
        if k == 0: break

        m -= 1
    return arr



print(KswapPermutation([4, 5, 2, 1, 3], 5, 3))