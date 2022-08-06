"""
Repeated Character

Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

Input:
S = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating
characters. Out of these, g occurs first.
"""
from collections import Counter
def firstRep(s):

    d = Counter(s)
    if set(d.values()) == {1}: return -1
    for item in s:
        if d[item] > 1: return item

print(firstRep('geeksforgeeks'))
