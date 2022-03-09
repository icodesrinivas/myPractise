# You wish to buy video games from the famous online video game store Mist.
#
# Usually, all games are sold at the same price,  dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game will cost  dollars, and every subsequent game will cost  dollars less than the previous one. This continues until the cost becomes less than or equal to  dollars, after which every game will cost  dollars. How many games can you buy during the Halloween Sale?


def howManyGames(p, d, m, s):
    cost = 0
    gift = 0
    while cost < s:
        cost = cost + p
        p = m if p-d <= m else p - d
        if cost <= s:
            gift += 1
    print(gift)

# howManyGames(73, 72, 44, 9163)
howManyGames(1, 1, 1, 9190)