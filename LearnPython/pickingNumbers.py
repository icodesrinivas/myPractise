from collections import Counter
from functools import reduce
def pickingNumbers(a):
    max_count = max(Counter(a).values())
    a = sorted(Counter(a).items(), key=lambda v: v[0])

    max_count = [max(a[i][1] + a[i+1][1], max_count) for i in range(len(a)-1) if abs(a[i][0] - a[i+1][0]) == 1][0]

    print(max_count)
    return max_count



a = [1,1,2,2,2,2,4,4,5,5]
a = '4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97'.split()
a = list(map(int, a))
pickingNumbers(a)