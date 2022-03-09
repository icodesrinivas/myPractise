# import random
#
# a = [1,2,3,4,5]
# random.shuffle(a)
# print(a)
# # print(a[3:0:-1])
#
# def f(i, values = []):
#     values.append(i)
#     print (values)
#     return values


data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v


print(fun(data[0]))

a=[1,2,3,4,5,6,7,8,9]
print(a[::2])

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(data[0])
print(data[0][0][0])


fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1

fruit_list2[0] = 'Guava'
print(fruit_list2)
print(fruit_list1)

def f(value, values):
    v = 1
    value = 33
    values[1] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[1])