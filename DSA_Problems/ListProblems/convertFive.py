"""
Replace all 0's with 5

You are given an integer N. You need to convert all zeroes of N to 5.

Example 1:

Input:
N = 1004
Output: 1554
Explanation: There are two zeroes in 1004
on replacing all zeroes with "5", the new
number will be "1554".

Expected Time Complexity: O(K) where K is the number of digits in N
Expected Auxiliary Space: O(1)
"""

def convertFive(n):

    ans = 0
    i = 0

    while n!=0:
        d = n%10
        if d == 0:
            ans += (5*(10**i) if i>0 else 5)
        else:
            ans += (d*(10**i) if i>0 else d)
        n = n//10
        i += 1
    return ans

print(convertFive(121))