# Find the least number of switch/cost required to make all the bulbs on.
# eg., [1,0,1] --> [1,1,1] in 2 switch/cost
def bulbs(A):

    switch = 0
    i = 0
    while i < len(A):

        b = A[i]
        if b == 0 and switch % 2 == 0:
            b = A[i]
        if b == 1 and switch % 2 == 1:
            b = not A[i]

        if b == 1:
            pass
        else:
            switch += 1

        i += 1

    return switch

print(bulbs([0,1,0,1,1,0,1,1]))

def bulbs2(A):

    cost = 0

    for b in A:
        if cost%2 == 0: b = b
        else: b = not b

        if b%2 == 1: continue
        else: cost += 1

    return cost

print(bulbs2([0,1,0,1,1,0,1,1]))