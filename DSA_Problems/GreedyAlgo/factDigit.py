"""
Fact Digit Sum

A(X) for positive integer X is the sum of factorials of its digits. For example, A(154) = 1! + 5! + 4!= 145.
Given a number N, find the minimum number X such that A(X) = N.

Input: N = 40321
Output: 18
Explanation: A(18)=1!+ 8! =40321
Note that A(80) and A(81) are also
40321, But 18 is the smallest
number.
"""

def FactDigit(N):
    i = 9
    fac = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    ans = ''
    while i > 0:
        if fac[i] <= N:
            ans += str(i) * (N//fac[i])
            N = N%fac[i]
        if N == 0: return ans[::-1]
        i -= 1









print(FactDigit(444444))