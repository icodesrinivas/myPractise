"""
Maximize Toys

Given an array arr[ ] of length N consisting cost of N toys and an integer K depicting the amount with you. Your task is to find maximum number of toys you can buy with K amount.

Input:
N = 7
K = 50
arr[] = {1, 12, 5, 111, 200, 1000, 10}
Output: 4
Explaination: The costs of the toys
you can buy are 1, 12, 5 and 10.
"""

def toyCount(N, K, arr):

    arr.sort()

    toy_count = 0
    total_cost = 0

    for toy_cost in arr:
        total_cost += toy_cost
        if total_cost > K:
            break
        toy_count += 1

    return toy_count



print(toyCount(3, 100, [20, 30, 50]))

