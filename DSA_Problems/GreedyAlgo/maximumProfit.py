"""
Theft at World Bank

The worlds most successful thief Albert Spaggiari was planning for his next heist on the world bank. He decides to carry a sack with him, which can carry a maximum weight of C kgs. Inside the world bank there were N large blocks of gold. All the blocks have some profit value associated with them i.e. if he steals ith block of weight w[i] then he will have p[i] profit. As blocks were heavy he decided to steal some part of them by cutting them with his cutter.
The thief does not like symmetry, hence, he wishes to not take blocks or parts of them whose weight is a perfect square. Now, you need to find out the maximum profit that he can earn given that he can only carry blocks of gold in his sack.
Note: The answer should be precise upto 3 decimal places.

N = 3, C = 10
w[] = {4, 5, 7}
p[] = {8, 5, 4)
Output:
7.857
Explanation: As first blocks weight is 4
which is a perfect square, he will not use
this block. Now with the remaining blocks
the most optimal way is to use 2nd block
completely and cut 5kg piece from the 3rd
block to get a total profit of 5 + 2.857
= 7.857
"""
import math
def maximumProfit(N, C, w, p):

    wp = list(zip(w,p))

    wp = [(p/w, w, p) for w, p in wp]
    wp = sorted(wp, key=lambda x:-x[0])

    total_p = 0
    for d, w, p in wp:
        if not math.sqrt(w).is_integer():
            if w < C:
                C -= w
                total_p += p
            else:
                total_p += round((C / w) * p, 3)
                C = 0
    return total_p

print(maximumProfit(3, 10, [4, 5, 7], [8, 5, 4]))
