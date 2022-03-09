
from collections import Counter


lis = [1,2,1,2,1,3,14,5,6,7]

result = Counter(lis)
print(result[1])


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = 10
N = list(map(int, '2 3 4 5 6 8 7 6 5 18'.split(' ')))
xi = 6
shoe_counter = Counter(N)
profit = 0
for _ in range(xi):
    shoe_size = list(map(int, input().split()))
    print(shoe_size)
    if shoe_size[0] in N and shoe_counter[shoe_size[0]] > 0:
        profit += shoe_size[1]
        shoe_counter[shoe_size[0]] -= 1
print(profit)