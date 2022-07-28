"""
Largest number possible

Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'.

Input: N = 2, S = 9
Output: 90
Explaination: It is the biggest number
with sum of digits equals to 9.
"""

def findLargest(N, S):
    if S == 0 and N > 1: return -1

    nines = S // 9
    rem = S % 9

    output = ''
    i = 1
    while i <= N:
        if nines > 0:
            output += '9'
            nines -= 1
        elif rem != 0:
            output += str(rem)
            rem = 0
        else:
            output += '0'

        i += 1

    if nines > 0 or rem != 0: return -1

    return int(output)




def findLargest2(N, S):
    if S > 9 * N: return -1
    if S == 0 and N > 1: return -1

    return (10**N - 1) - ((10**(((N*9)-S)//9)) - 1) - ((((N*9)-S)%9) * (10**(((N*9)-S)//9)))

print(findLargest2(3, 13))



