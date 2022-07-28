
"""
Smallest number with sum of digits as N and divisible by 10^N

Find the smallest number such that the sum of its digits is N and it is divisible by 10N.

Input: N = 5
Outptut: 500000
Explanation: Sum of digits of 500000
is 5 and divisible by 105
"""

def digitsNum(N):

    # if N <= 9: return str(N) + ('0' * (N))

    return  str(N%9 if N%9>0 else '') + str('9' * (N//9)) + ('0' * (N))


print(digitsNum(18))
