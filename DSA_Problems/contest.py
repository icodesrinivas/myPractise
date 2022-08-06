

def minimumOperations(nums):

    if list(set(nums)) == [0]:
        return 0

    min_n = min(nums)
    max_n = max(nums)

    if min_n == max_n:
        return 1

    count = 0

    while not all([i==0 for i in nums]):
        if any([i%2==1 for i in nums]):
            nums = [i-1 for i in nums if i>0]
            count += 1
        else:
            max_n = max(nums)
            count += (max_n//2)
            nums = [0 for i in nums]

    return count

print(minimumOperations([1,5,0,3,5]))
#
# def maximumGroups(grades):
#
#     if len(grades) <= 2:
#         return 1
#
#     grades = sorted(grades)
#
#     i = 0
#     j = 1
#     n = len(grades)
#     count = 0
#     max_grade = 0
#     while i < n:
#         if sum(grades[i: i+j if i+j<n else n-1]) > max_grade:
#             max_grade = sum(grades[i: i+j if i+j<n else n-1])
#             if i+j <= n: count += 1
#
#         i += j
#         j += 1
#     return count
#
# print(maximumGroups([47,2,16,17,41,4,38,23,47]))
# print(maximumGroups([10,6,12,7,3,5]))
