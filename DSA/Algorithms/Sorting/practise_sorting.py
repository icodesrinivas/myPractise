
def bubble_sort(nums):

    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums

# print(bubble_sort([5,9,3,1,2,8,4,7,6]))


def selection_sort(nums):

    for i in range(len(nums)-1, 0, -1):
        max_index = i
        for j in range(i):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[max_index], nums[i] = nums[i], nums[max_index]

    return nums

print(selection_sort([5,7,4,3,8,6,1,9,2]))

def insertion_sort(nums):

    for i in range(1, len(nums)):

        anchor = i
        j = i



