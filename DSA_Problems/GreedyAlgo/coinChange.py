# Find the minimum coins required to reach total money
# Coin Dinominations are {1,2,5,10,20,50,100,1000}

def coinChange(money, d):

    coin_count = 0

    for i in range(len(d)-1, -1, -1):
        factor = 0
        if d[i] <= money:
            factor = money // d[i]
            coin_count += factor
            money -= (d[i] * factor)

        if money == 0:
            return coin_count

print(coinChange(2035, [1,2,5,10,20,50,100]))

