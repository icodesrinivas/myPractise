
def isValid(s):

    if len(s) % 2 != 0:
        return False

    start = 0
    end = len(s) - 1

    brackets = {'[': ']', '{': '}', '(': ')'}

    while start < end:
        if s[end] == brackets[s[start]]:
            start += 1
            end -= 1
        else:
            return False

    return True

# print(isValid('([{()}])'))

def isValidParantheses(s):

    if len(s) % 2 != 0:
        return False

    stack = []

    bracket = {'[':']', '(':')', '{':'}'}

    for i in range(len(s)):

        if s[i] in bracket.values() and len(stack) == 0:
            return False

        if s[i] in bracket.keys():
            stack.append(s[i])
        else:
            if s[i] == bracket[stack[-1]]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

print(isValidParantheses('()[]{}'))
print(isValidParantheses('([{()}])'))
print(isValidParantheses('){'))


