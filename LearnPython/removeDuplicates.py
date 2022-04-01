
l = [1,2,2]
# k.pop(5)
# k.append('_')
# print(k)

def removeDuplicates1(nums):
    i = 1
    dup = 0
    count = 1

    # Edge Cases
    if len(nums) == 1:
        return 1
    if len(nums) == 0:
        return 0

    while i < len(nums):
        if nums[i] == nums[i - 1]:
            dup += 1
        else:
            if nums[i] != '_':
                count += 1
            while dup > 0:
                nums.pop(i - dup)
                nums.append('_')
                i -= 1
                dup -= 1
        i += 1

    # If a single number duplicate case
    if dup > 0 and '_' not in nums:
        nums = list(set(nums))
        return len(nums)

    nums = [nums[i] for i in range(len(nums)) if nums[i] != '_']

    return nums, count

# print(removeDuplicates(l))

# 3 pointer solution
def removeDuplicates(nums):

    uniqueIndex = 0
    prevIndex = 0
    currentIndex = 1

    if len(nums) == 0:
        return 0

    for i in range(1, len(nums)):

        if nums[prevIndex] == nums[currentIndex]:
            prevIndex = currentIndex
            currentIndex += 1
        else:
            uniqueIndex += 1
            nums[uniqueIndex] = nums[currentIndex]
            prevIndex = currentIndex
            currentIndex += 1

    return uniqueIndex + 1

k = [1]
print(removeDuplicates(k))

