
a_list = ["12", "34", "44"]

def string_to_integer(s):

    num = 0
    size = len(s)

    for item in s:

        num = (num * 10) + (ord(item) - 48)

    return num

# result = list(map(lambda x:string_to_integer(x), a_list))
# print(result)

def sq(a):
    return a*a

def cube(b):
    return b*b*b

func_list = [sq, cube]

lis = [1,2,3,4,5,6]


for i in range(1, len(lis)+1):
    print(list(map(lambda x:x(i), func_list)))
