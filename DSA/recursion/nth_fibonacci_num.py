
# def fib(num, call):
#     print('num:', num, call)
#     if num < 2:
#         return num
#     else:
#         return fib(num - 1, f'function: f(num-1) f{num-2}') + fib(num - 2, f'function: {num-1} f(num-2)')

# print(fib(6, 'initial'))

# 4 + 6
# 3 + 3
# 2 + 1
# 1 + 0

def fib(num, st, en):
    if num == 1:
        return en
    else:
        temp_st = en
        en += st
        return fib(num-1, temp_st, en)

print(fib(28, 0, 1))