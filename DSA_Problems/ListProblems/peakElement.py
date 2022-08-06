"""
Peak element

An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0.


Example 1:

Input:
N = 3
arr[] = {1,2,3}
Possible Answer: 2
Generated Output: 1
Explanation: index 2 is 3.
It is the peak element as it is
greater than its neighbour 2.
If 2 is returned then the generated output will be 1 else 0.

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)
"""

def findPeakUtil(arr, low, high, n):

    mid = low + (high - low) / 2
    mid = int(mid)
    print('mid',mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
    else:
        return findPeakUtil(arr, (mid + 1), high, n)

def peakElement(arr, n):
    return findPeakUtil(arr, 0, n - 1, n)

print(peakElement([1, 13], 2))