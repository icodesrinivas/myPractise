
"""
Shop in Candy Store

In a candy store, there are N different types of candies available and the prices of all the N different types of candies are provided to you.
You are now provided with an attractive offer.
You can buy a single candy from the store and get at most K other candies ( all are different types ) for free.
Now you have to answer two questions. Firstly, you have to find what is the minimum amount of money you have to spend to buy all the N different candies. Secondly, you have to find what is the maximum amount of money you have to spend to buy all the N different candies.
In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.

Input:
N = 4
K = 2
candies[] = {3 2 1 4}

Output:
3 7

Explanation:
As according to the offer if you buy
one candy you can take at most two
more for free. So in the first case,
you buy the candy which costs 1 and
takes candies worth 3 and 4 for free,
also you buy candy worth 2 as well.
So min cost : 1+2 =3.
In the second case, you can buy the
candy which costs 4 and takes candies
worth 1 and 2 for free, also you need
to buy candy worth 3 as well.
So max cost : 3+4 =7.
"""

def candyStore(candies, N, K):
    candies.sort()
    start = 0
    end = N - 1

    min_cost = 0

    while start <= end:
        min_cost += candies[start]
        start += 1
        end -= K

    max_cost = 0
    start = 0
    end = N - 1
    while start <= end:
        max_cost += candies[end]
        end -= 1
        start += K

    return min_cost, max_cost


print(candyStore([3, 2, 1], 3, 3))

