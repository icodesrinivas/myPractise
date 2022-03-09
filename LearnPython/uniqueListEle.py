# Valdiate whether all the elements in the list are unique
from collections import Counter
myList = [1,2,3,4,5,6,7]
myList = Counter(myList)
def checkUniqueListEle(myList):
    return all(map(lambda x: myList[x] < 2, myList))

print(checkUniqueListEle(myList))