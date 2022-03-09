def string_to_integer(s):

    num = 0
    size = len(s)

    for item in s:

        num = (num * 10) + (ord(item) - 48)
    print(type(num))
    return num

print(string_to_integer('123'))