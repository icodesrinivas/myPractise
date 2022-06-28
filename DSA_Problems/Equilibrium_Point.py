

def equilibriumPoint(A, N):

    if N == 1:
        return 1

    left = 0
    right = N - 1

    left_total = A[left]
    right_total = A[right]

    while left < right:
        if left_total == right_total:
            left += 1
            right -= 1
            left_total += A[left]
            right_total += A[right]
        elif left_total > right_total:
            right -= 1
            right_total += A[right]
        else:
            left += 1
            left_total += A[left]

    if left_total == right_total and left == right:
        return left + 1
    else:
        return -1

lis = '20 17 42 25 32 32 30 32 37 9 2 33 31 17 14 40 9 12 36 21 8 33 6 6 10 37 12 26 21 3'.split(' ')
lis = list(map(int, lis))

print(equilibriumPoint(lis, 30))


# Python program to find the equilibrium
# index of an array

# function to find the equilibrium index
def equilibrium(arr):

    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):

        total_sum -= num

        if total_sum == left_sum:
            return i+1

        left_sum += num

    return -1


# Driver code
arr = [1,3,5,2,2]
print('First equilibrium index is ',
      equilibrium(arr))

# This code is contributed by Abhishek Sharma
