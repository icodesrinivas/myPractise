score_list = [['Harry', 1], ['Berry', 2], ['Kerry', 2]]


# # My Solution
# count = 0
# lowest = 0
# second_lowest = 0
# for score in score_list:
#     if count == 0:
#         lowest = second_lowest = score[1]
#     elif score[1] < lowest:
#         second_lowest = lowest
#         lowest = score[1]
#     elif score[1] > lowest and score[1] < second_lowest:
#         second_lowest = score[1]
#     elif lowest == second_lowest and score[1] > lowest:
#         second_lowest = score[1]
#     else:
#         pass
#     count += 1
#
# result = [score[0] for score in score_list if score[1] == second_lowest]
# result.sort()
#
# for name in result:
#     print(name)

# Best Solution

second_lowest = list(set([score[1] for score in score_list]))
second_lowest.sort()
second_lowest = second_lowest[1]
result = [score[0] for score in score_list if score[1] == second_lowest]
result.sort()

for name in result:
    print(name)
