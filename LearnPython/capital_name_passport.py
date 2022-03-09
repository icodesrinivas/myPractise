import os
# Complete the solve function below.
def solve(s):
    # s = s.split()
    # for index in range(len(s.split(' '))):
    #     if s[index][0].isdigit() == False:
    #         s[index] = s[index][0].capitalize() + s[index][1:]
    # print(s)

    # words = s.split(" ")
    # capitalized_words = [w.capitalize() for w in words]
    # print(" ".join(capitalized_words))
    # return " ".join(capitalized_words)

    print(' '.join(list(map(lambda x:x.capitalize(), s.split(" ")))))


if __name__ == '__main__':
    s = 'alison    heck   apsdasd 2313'

    result = solve(s)