
def longestCommonPrefix(arr, n):
    longest_prefix = arr[0]

    for arr_index in range(1, n):

        string = arr[arr_index]

        if len(string) < len(longest_prefix):longest_prefix=longest_prefix[0:len(string)]

        for i in range(len(longest_prefix)):
            if string[i] != longest_prefix[i]:
                longest_prefix = longest_prefix[0:i]
                break

    if len(longest_prefix) == 0:
        return -1

    return longest_prefix







    return longest_prefix

print(longestCommonPrefix(['apple', 'ape', 'april'], 3))
