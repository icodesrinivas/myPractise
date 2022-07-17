#  There is a row of empty (.) and filled (x) seats.
# Find the minimum number of moves required to make people sit together

def minimumJump(seats):

    position = [i for i, v in enumerate(seats) if v=='x']

    med_i = len(position) // 2

    med_v = position[med_i]

    jumps = 0

    for i in range(len(position)):

        start = position[i]
        end = med_v - med_i + i

        jumps += abs(start - end)

    return jumps


s = '. . x . x . . x x . . . x . .'.split()
print(minimumJump(s))
