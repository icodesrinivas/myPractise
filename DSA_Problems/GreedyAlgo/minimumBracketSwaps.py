"""
Minimum Swaps for Bracket Balancing

You are given a string S of 2N characters consisting of N ‘[‘ brackets and N ‘]’ brackets. A string is considered balanced if it can be represented in the for S2[S1] where S1 and S2 are balanced strings. We can make an unbalanced string balanced by swapping adjacent characters. Calculate the minimum number of swaps necessary to make a string balanced.
Note - Strings S1 and S2 can be empty.

Input  : []][][
Output : 2
Explanation :
First swap: Position 3 and 4
[][]][
Second swap: Position 5 and 6
[][][]
"""
def minimumSwaps(S):

    swap = 0
    open = 0

    for i in S:
        if i == '[':
            open += 1
        else:
            open -= 1
            if open < 0: swap -= open

    return swap

print(minimumSwaps(']]][[['))


print(minimumSwaps('[]]][][['))


