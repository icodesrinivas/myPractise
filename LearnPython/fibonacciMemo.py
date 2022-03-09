

def fib(n, memo):
    if n==0:
        return 0
    if n==1:
        return 1

    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    print(memo)
    return memo[n]

print(fib(6, {}))