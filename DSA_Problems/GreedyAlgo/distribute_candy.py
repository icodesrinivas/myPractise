
# N kids stand in a line each having an integer rating, distribute the candies based on below,
# Each kid gets at least 1 candy
# Kinds with higher ratings than theie neighbours get more candies
# find minimim candies required

def candy(A):

    n = len(A)
    data = sorted((i, x) for i, x in enumerate(A))

    candies = [1] * n

    for i, _ in data:
        if i > 0 and A[i] > A[i-1]:
            candies[i] = max(candies[i], candies[i-1] + 1)

        if i < n-1 and A[i] > A[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)

print(candy([1,3,7,1]))