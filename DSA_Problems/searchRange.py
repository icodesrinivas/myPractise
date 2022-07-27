
# Find First and Last Position of Element in Sorted Array
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

def searchRange(nums, target):


    start = 0
    end = len(nums) - 1

    ans = [-1, -1]

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            i = j = mid
            while i >= 0 and nums[i] == target:
                i -= 1
            while j <= len(nums)-1 and nums[j] == target:
                j += 1
            ans[0] = i + 1
            ans[1] = j - 1
            break
        else:
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return ans

print(searchRange([1], 2))


