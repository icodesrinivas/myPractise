
def jumpingOnClouds(c):
    i = jumps = 0
    while i != len(c)-1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i = i + 2
        else:
            i += 1
        jumps += 1
    return jumps

print(jumpingOnClouds([]))
