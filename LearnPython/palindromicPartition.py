
def checkPalindrom(s):
    print(s)
    if len(s) == 1:
        return True
    if s[0] == s[len(s)-1]:
        return checkPalindrom(s[1:len(s)-1])
    else:
        return False


def palindromicPartition(s, memo):
    print('string', s)
    if len(s) <= 1:
        memo[s] = True
        return s


print(palindromicPartition('geeks', {}))
# k = 'ks'
# print(k[1:len(k)])
# print(s[1:len(s)-1])
# print(checkPalindrom('itia'))

# s = 'sas'
# print(checkPalindrom(s))
# print(s[:len(s)-1])
# print(s[1:len(s)])