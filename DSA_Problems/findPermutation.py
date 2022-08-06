"""
Permutations of a given string

Given a string S. The task is to print all permutations of a given string in lexicographically sorted order.

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6
forms as ABC, ACB, BAC, BCA, CAB and CBA .
"""

def find_permutation(S):
    ans = []
    s = list(S)

    loop = len(S) * (len(S)-1)

    while loop > 0:
        for i in range(len(s) - 1):
            s[i], s[i + 1] = s[i + 1], s[i]
            ans.append("".join(s))
            loop -= 1

    return sorted(set(ans))

print(find_permutation('ABB'))