
def jumpingOnClouds(c, k):
    e = 100
    n = 0
    first = True
    while n != 0 or first:
        if c[n] == 1:
            e = e -1 - 2
        else:
            e = e -1
        n = (n+k)%len(c)
        first = False
    return e

    # for i in range(0, len(c), k):
    #     e = e - 1 - 2 * c[i]
    # return e

print(jumpingOnClouds([1,1,1,0,1,1,0,0,0,0], 3))

