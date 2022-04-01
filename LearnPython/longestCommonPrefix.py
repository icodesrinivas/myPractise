# My Solution
def longestCommonPrefix(strings):
    common = strings[0]
    output = ''
    for string in strings[1:]:
        index = 0
        output = ''
        while index < len(string) and index < len(common):
            if string[index] == common[index]:
                output = output + string[index]
                index += 1
            else:
                break

        common = output

    return common

# print(longestCommonPrefix(["leets","leetcode","leet","lee"]))

# Understanding LeetCode Solutions
# 1. Horizontal Scanning
def longestCommonPrefix1(strings):
    if len(strings) == 0: return ""

    prefix = strings[0]

    for i in range(1, len(strings)):
        try:
            strings[i].index(prefix)


print('flower'.index('flow'))