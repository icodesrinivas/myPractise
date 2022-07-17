

def majorityEle(A):
    count = 0
    ele = 0

    for i in range(len(A)):

        if count == 0:
            ele = A[i]

        if ele == A[i]:
            count += 1
        else:
            count -= 1

    ele_count = 0
    for num in A:
        if ele == num:
            ele_count += 1
    if ele_count > len(A) // 2:
        return ele
    else:
        return -1

s = '17 2 9 2 3 2 17 2 18 2 18 2 3 2 3'.split()
# s = '3 2 3'.split()
s = list(map(int, s))
print(majorityEle(s))



def majorityElement(A):

    n = len(A)
    ans = 0

    for b in range(32):
        ones = 0
        for num in A:
            if (1 << b) & num:
                ones += 1

        if ones > n//2:
            ans += (1 << b)

    return ans


def majEle(A):


    A.sort()

    curr_max = 1
    final_max = 1
    prev_ele = A[0]
    max_ele = A[0]

    for i in range(1, len(A)):

        if A[i] == prev_ele:
            curr_max += 1
            if curr_max > final_max:
                max_ele = A[i]
                final_max += 1
        else:
            curr_max = 1

        prev_ele = A[i]

        if final_max > len(A) // 2:
            return max_ele

    return -1




