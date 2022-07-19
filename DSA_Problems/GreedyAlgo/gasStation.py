
def canCompleteCircuit(gas, cost):

    prev_gas = 0
    prev_cost = 0

    starting_gas = 0

    N = len(gas)

    for i, (g, c) in enumerate(zip(gas*2, cost*2)):

        if i == starting_gas + N:
            return starting_gas

        if i > starting_gas:
            g = prev_gas + g - prev_cost

        if g < c:
            starting_gas = i + 1

        if starting_gas >= N:
            return -1

        prev_gas = g
        prev_cost = c

    return -1

gas = [3,5,2,1,7]
cost = [4,2,1,9,1]

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))