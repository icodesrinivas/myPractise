import time



def integer_to_string(i):

    # Edge case
    if i == 0:
        return chr(i+48)

    negative_integer = False

    if i < 0:
        negative_integer = True
        i = - i

    result = ''
    while i > 9:

        result = chr((i%10) + 48) + result
        i = i // 10
        if i < 10:
            result = chr(i+48) + result

    if negative_integer:
        result = '-' + result

    return result
# start_time = time.perf_counter()
# print(integer_to_string(-22342), type(integer_to_string(-22342)))
# end_time = time.perf_counter()
# print(f'{end_time - start_time}')

def integer_to_string(i):

    # Edge case
    if i == 0:
        return chr(i+48)

    # Handling negative number
    negative_integer = False
    if i < 0:
        negative_integer = True
        i = - i

    def convert_to_string(i):
        if i < 9:
            return chr(i+48)
        else:
            return (convert_to_string(i // 10)) + chr((i%10)+48)

    result = convert_to_string(i)

    if negative_integer:
        return '-' + result
    else:
        return result

start_time = time.perf_counter()
print(integer_to_string(-121))
end_time = time.perf_counter()
print(f'{end_time - start_time}')

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n-1)
# print(factorial(4))

