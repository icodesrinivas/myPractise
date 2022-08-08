
"""
Maximize sum(arr[i]*i) of an Array

Given an array A of N integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where i = 0, 1, 2,., n 1.
You are allowed to rearrange the elements of the array.
Note: Since output could be large, hence module 109+7 and then print answer.



Example 1:

Input : Arr[] = {5, 3, 2, 4, 1}
Output : 40
Explanation:
If we arrange the array as 1 2 3 4 5 then
we can see that the minimum index will multiply
with minimum number and maximum index will
multiply with maximum number.
So 1*0+2*1+3*2+4*3+5*4=0+2+6+12+20 = 40 mod(109+7) = 40
"""

def Maximize(a, n):
    a.sort()
    print(a)
    res = 0
    for i in range(n-1, 0, -1):
        res += a[i] * i
    return res%((10**9)+7)

a = '6 6 8 19 8 10 19 14 20 18 5 11 20 6 10 7 15 8 8 9'.split()
a = list(map(int, a))
print(Maximize(a, 20))
