
def canReach(A, N):
    n = N - 1
    for i in range(n - 1, -1, -1):
        if A[i] + i >= n:
            n = i

    if n == 0:
        return 1
    else:
        return 0

# lis = '5 9 3 2 1 0 2 3 3 1 0 0'.split(' ')
# lis = list(map(int, lis))
# print(canReach(lis, len(lis)))

def canReach2(lis, n):

    reachable = 0

    for i in range(n):
        reachable = max(reachable, i + lis[i])
        if i >= reachable:
            return 'false'
    return 'true'

print(canReach2([3, 0, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11))

def jump(nums):
    reachable = nums[0]
    steps = nums[0]
    jumps = 1

    if len(nums) == 1: return 0

    for i in range(1, len(nums)):

        if i==len(nums)-1: return jumps

        reachable = max(i+nums[i], reachable)
        steps -=1

        if steps == 0:
            jumps += 1
            steps = reachable - i

print(jump([2,3,1,1,4]))

