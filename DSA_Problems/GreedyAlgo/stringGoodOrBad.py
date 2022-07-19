# Good or Bad string
"""
If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD".
A String is considered "GOOD" only if it is not “BAD”.
"""

def isGoodOrBad(S):
    consonent = 0
    vowel = 0
    for val in S:

        if val in 'aeiou' or val == '?':
            vowel += 1
            if vowel > 5:
                return 0
            else:
                consonent = 0
        if val not in 'aeiou?' or val == '?':
            consonent += 1
            if consonent > 3:
                return 0
            else:
                vowel = 0

    return 1




print(isGoodOrBad('?c?a'))


def isGoodOrBad2(S):
    count = 0
    count1 = 0
    v = 'aeiou'
    for i in S:
        if i in v or i == '?':
            count += 1
            if count > 5:
                return 0
        else:
            count = 0
        if i not in v or i == '?':
            count1 += 1
            if count1 > 3:
                return 0
        else:
            count1 = 0
    return 1

print(isGoodOrBad2('?c?a'))

