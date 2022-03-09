# def callme(n):
#     if n < 1:
#         print(f'I am {n} now')
#     else:
#         callme(n-1)
#         print(n)
#
# callme(5)

# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))

def fibonacci(n):
    if n == 1:
        return 1
    else:
        return n + fibonacci(n-1)

print(fibonacci(4))
