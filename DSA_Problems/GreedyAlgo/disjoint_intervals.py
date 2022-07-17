

# Given a list of intervals, find the length of the maximal set of mutually disjoint intervals.

def disjoint(A):

    A.sort(key=lambda x: x[1])

    prev_s = A[0][0]
    prev_e = A[0][1]

    ds = 1

    for s, e in A:
        if s <= prev_e and prev_s :
            pass
        else:
            prev_s = s
            prev_e = e
            ds += 1

    return ds
print(disjoint([[1,2], [2,19], [4,6]]))