def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False


    revertNumber = 0
    while x > revertNumber:
        revertNumber = (revertNumber * 10) + (x % 10)
        x = x // 10

    return (x == revertNumber) or (x == revertNumber // 10)

print(isPalindrome(100))
