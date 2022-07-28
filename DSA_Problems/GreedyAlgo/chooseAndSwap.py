"""
You are given a string s of lower case english alphabets. You can choose any two characters in the string
and replace all the occurences of the first character with the second character and replace all the occurences
of the second character with the first character. Your aim is to
find the lexicographically smallest string that can be obtained by doing this operation at most once.

Input:
A = "ccad"
Output: "aacd"
Explanation:
In ccad, we choose a and c and after
doing the replacement operation once we get,
aacd and this is the lexicographically
smallest string possible.
"""

def chooseAndSwap(A):

    s = sorted(set(A))
    swap_a = None
    swap_b = None
    for item in A:
        if ord(item) > ord(s[0]):
            swap_a = item
            swap_b = s[0]
            break
        elif ord(item) == ord(s[0]): s.pop(0)
        if len(s) == 0: return A

    A = list(A)
    for index in range(len(A)):
        if A[index] == swap_a: A[index] = swap_b
        elif A[index] == swap_b: A[index] = swap_a

    return "".join(A)


print(chooseAndSwap('kkxo'))




