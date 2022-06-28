

# def maxLen(n, arr):
#
#     result = 0
#
#     if sum(arr) == 0:
#         return len(arr)
#
#     for left in range(n):
#         right = n - 1
#         while right >= left:
#             total_sum = sum(arr[left:right+1])
#             arr_len = len(arr[left:right+1])
#             if total_sum == 0:
#                 if arr_len > result:
#                     result = arr_len
#                     break
#             right -= 1
#
#     return result


def maxLen(n, arr):

    max_length = 0
    index_dict = {}
    sum = 0
    for i in range(n):

        sum += arr[i]

        if arr[i] == 0 and max_length == 0:
            max_length = 1

        if sum == 0:
            max_length = i + 1

        if sum not in index_dict:
            index_dict[sum] = i
        else:
            max_length = max(max_length, i - index_dict[sum])

    return max_length
lis = '-776 794 387 -648 363 691 764 -539 -171 -210 -566 783 -861 68 930 -21 -68 394 -10 -228 422 785 199 -314 -412 -90 -955 863 -995 306 85 337 847 314 125 583 815 435 -42 -86 -275 -787 -402 755 933 -675 -738 -225 -93 796 -433 -466 98 -316 -651 -300 -285 866 445 441 32 98 482 710 568 -496 587 307 220 -527 733 504 271 -707 341 797 619 847 922 380 -763 -840 -192 -33'.split(' ')
lis = list(map(int, lis))
print(maxLen(2, [23, -23]))

# print(sum([-2,2,-8,1,7,10]))