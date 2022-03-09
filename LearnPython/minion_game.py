def minion_game(string):
    # Learning : Use of len(string[x:]) was very expensive
    # stuart_score = sum([len(string[x:]) for x in range(len(string)) if string[x] not in 'AEIOU'])
    #
    # kevin_score = sum([len(string[x:]) for x in range(len(string)) if string[x] in 'AEIOU'])
    string_len = len(string)
    stuart_score = 0
    kevin_score = 0
    for x in range(len(string)):
        score = string_len - x
        if string[x] not in 'AEIOU':
            stuart_score += score
        else:
            kevin_score += score
    print(stuart_score)
    print(kevin_score)
minion_game('BAANANAS')
#
# stuart_score = 8 + 5 + 3 + 1 = 17
#
# kevin_score = 7 + 6 + 4 + 2 = 19

