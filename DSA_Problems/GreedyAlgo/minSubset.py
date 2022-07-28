

"""
Smallest Subset with Greater Sum

You are given an array Arr of size N containing non-negative integers. Your task is to choose the minimum number of elements such that their sum should be greater than the sum of the rest of the elements of the array.

Input:
N = 5
Arr[] = {4,3,1,0,2}
Output:
2
Explanation:
If we just select 4 and 3 from the array,
the sum will be (4+3) = 7 and the sum of
the rest of the elements will be (2+0+1)=3.
So, the answer will be 2. We can also
select 4 and 2 as well.
"""

def minSubset(A, N):

    A.sort()
    half = sum(A) // 2
    ans = 0
    t_sum = 0
    for i in range(N-1, -1, -1):
        if t_sum <= half:
            ans += 1
            t_sum += A[i]
        else:break


    return ans

print(minSubset([3,3,4,0,1], 5))