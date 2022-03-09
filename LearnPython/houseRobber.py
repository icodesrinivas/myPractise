

def houseRobber(houses, currentHouse):
    if currentHouse >= len(houses):
        return 0
    print('houses[currentHouse] + currentHouse', houses[currentHouse], currentHouse)
    selectFirstHouse = houses[currentHouse] + houseRobber(houses, currentHouse + 2)
    skipFirstHouse = houseRobber(houses, currentHouse + 1)
    return max(selectFirstHouse, skipFirstHouse)

houses = [6,7,1,30]

print(houseRobber(houses, 0))



