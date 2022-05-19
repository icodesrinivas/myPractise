# def decor(fun):
#     def inner():
#         fun()
#         print('3')
#
#     return inner
#
# @decor
# def num():
#
#     print('1')
#     print('2')
#
# num()
#

# def decor(fun):
#     def inner():
#         res = fun() + 5
#         return res
#     return inner
#
# @decor
# def num():
#     return 10
#
# print(num())


def decor(fun):
    def inner(a):
        b = 22
        res = fun(a) + b
        return res
    return inner

@decor
def num(a):
    return a

print(num(15))
