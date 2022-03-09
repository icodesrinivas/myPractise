
def power_of_num(n, m):
    if m == 1:
        return n
    else:
        return n * power_of_num(n, m-1)

print(power_of_num(10, 6))

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

print(power(2, 2))