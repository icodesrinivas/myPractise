"""
Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer.



Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def rotateArr(A, D, N):
    d = D % N
    g_c_d = gcd(D, N)
    for i in range(g_c_d):
        temp = A[i]
        j = i
        while True:
            k = (j+d)%N
            if k == i:
                break
            A[j] = A[k]
            j = k
            print('A',A)
        A[j] = temp

    return A
print(rotateArr([1,2,3,4,5,6,7,8,9,10,11], 2, 11))
