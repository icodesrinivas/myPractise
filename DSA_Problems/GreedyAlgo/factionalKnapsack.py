# Fractional Knapsack problem in python

def fractionalKnapsack(item_list, capacity):

    item_list.sort(key=lambda x: -x[2])

    total_value = 0

    for weight, value, density in item_list:
        if weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            ratio = capacity / weight
            total_value += (value * ratio)
            return total_value
    return total_value

print(fractionalKnapsack([(20, 100, 100//20), (30, 120, 120//30), (10, 60, 60//10)], 60))

