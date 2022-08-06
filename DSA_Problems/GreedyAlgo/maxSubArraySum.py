import sys
def maxSubArraySum(arr, N):

    max_sum = -(10**7)
    curr_sum = 0
    print('max_sum',max_sum)

    for i in range(N):
        curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum



# print(maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4], 9))
print(maxSubArraySum([-1,-2,-3,-4], 4))
# print(maxSubArraySum([1,2,3,-2,5], 5))
