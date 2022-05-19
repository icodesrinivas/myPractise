#
# # print('40.0'.isdigit())
# # result = '0.'.replace('.','').isdigit()
# # print(result)
# #
# # print(float('-+4.5'))
#
# # from collections import Counter
# #
# # print(Counter([10, 20, 20, 10, 10, 30, 50, 10, 20]))
# lis = [1,2,3,45]
# lis[0] = 22
# print(lis)
#
# string = "ABCD"
# print(string[0:2])
# string[0:2] = "KK"
# print(string)

# print(2.01 % 1 == 0)

# print(1 - (-1))

d = 123

k = d % 10
print(k)

result = ''

while d != 0:
    r = d % 10
    result = chr(ord('0') + r) + result
    d = d // 10



# print(result)

# print(''.join(map(str, [1,2,3,4,5])))


# add = lambda x, y : x+y
# print(add(5,2))
#
# add = lambda x : (lambda y: x + y)
#
# a = add(2)
# print(a(20))


# def add(x=10):
#     def another_add(y):
#         return x + y
#     return another_add
#
# x = add()
# print(x(20))
#
# b = 19
#
# def show(a):
#     print('b',b)
#     print(a(8))
#
# show(lambda x: x+5)
#
#
# print((lambda x,y: x+y)(5,2))

# def mult(func):
#     def inner(a,b):
#         r = a * b
#         print('mult', r)
#         result = func(a,b)
#         return result
#     return inner
#
# @mult
# def add(x,y):
#     return x+y
#
# print(add(5,2))

lst = [2, 22,33,1,10,12]

# new_lst = list(filter(lambda x: x>=10, lst))
# print(new_lst)

from functools import reduce

result = reduce(lambda m,n: m+n, lst)
print(result)