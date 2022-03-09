def add_sum(fun):
    def inner(a):
        val = fun(a)
        result = val + 5
        return result
    return inner


def num(val):
    return val

num = add_sum(num)
print(num(5))

