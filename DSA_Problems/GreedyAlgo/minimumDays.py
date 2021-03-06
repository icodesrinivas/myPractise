
"""
Check if it is possible to survive on Island

Ishika got stuck on an island. There is only one shop on this island and it is open on all days of the week except for Sunday. Consider following constraints:

N – The maximum unit of food you can buy each day.
S – Number of days you are required to survive.
M – Unit of food required each day to survive.
Currently, it’s Monday, and she needs to survive for the next S days.
Find the minimum number of days on which you need to buy food from the shop so that she can survive the next S days, or determine that it isn’t possible to survive.

nput: S = 10, N = 16, M = 2
Output: 2
Explaination: One possible solution is to
buy a box on the first day (Monday),
it’s sufficient to eat from this box up to
8th day (Monday) inclusive. Now, on the 9th
day (Tuesday), you buy another box and use
the chocolates in it to survive the 9th and
10th day.
"""
from math import ceil
def minimumDays(S, N, M):

    if M > N: return -1
    if S > 6 and (N - M) * 6 < M: return -1
    return ceil((S * M) / N)


print(minimumDays(48, 28, 24))

