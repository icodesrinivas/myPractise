# Little Bobby loves chocolate. He frequently goes to his favorite  store, Penny Auntie, to buy them. They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.

def chocolateFeast(n, c, m):
    chocolates = n // c
    wrappers = chocolates
    while wrappers>=m:
        chocolates += wrappers // m
        wrappers = wrappers // m + wrappers % m
    print(chocolates)
    # return wrappers

chocolateFeast(12,4,4)
chocolateFeast(7,3,2)