
def isPalindrome(string):
    n = len(string)
    if n < 2:
        return True
    else:
        if string[0].lower() != string[-1].lower():
            return False
        else:
            return isPalindrome(string[1:len(string)-1])

print(isPalindrome('Refer'))