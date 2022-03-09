

def countingValleys(steps, path):
    N = 0
    valley_count = 0
    for step in range(steps):
        N_old = N
        N = (N + 1) if path[step] == 'U' else (N - 1)
        if N_old == -1 and N == 0 : valley_count += 1

    return


countingValleys(12, 'DDUUUUDDDDUU')