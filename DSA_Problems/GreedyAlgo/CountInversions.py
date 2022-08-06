
"""
Count Inversions

Given an array of integers. Find the Inversion Count in the array.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5
has three inversions (2, 1), (4, 1), (4, 3).
"""

def inversionCount(arr, n):
    s_arr = sorted(arr)
    count = 0
    for i in range(n):
        if i < arr.index(s_arr[i]):
            count += (arr.index(s_arr[i]) - i)
        if i > arr.index(s_arr[i]):
            count += arr.index(s_arr[i])
    return count


arr = '468 335 1 170 225 479 359 463 465 206 146 282 328 462 492 496 443 328 437 392 105 403 154 293 383 422 217 219 396 448 227 272 39 370 413 168 300 36 395 204 312 323'.split(' ')

arr = list(map(int, arr))
print(inversionCount(arr, 42))