def swap_case(s):
    # MY SOLUTION 1
    # result = ''
    # for index in range(len(s)):
    #     if s[index].islower():
    #         result += s[index].upper()
    #     else:
    #         result += s[index].lower()
    # print(result)

    # MY SOLUTION 2
    print(''.join(map(lambda x: x.upper() if (x.islower()) else x.lower(), s)))

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)