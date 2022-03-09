def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    else:
        if isOdd(arr.pop()) == True:
            return True
        else:
            return someRecursive(arr, isOdd)

print(someRecursive([4,6,8,9], isOdd))