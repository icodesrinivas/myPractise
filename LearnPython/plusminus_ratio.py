
print('{:.3f}'.format(10/33))

def plusMinus(arr):
    # Write your code here
    (minus, plus, zero) = (len(list(filter(lambda x: x < 0, arr))), len(list(filter(lambda x: x > 0, arr))), len(list(filter(lambda x: x == 0, arr))))

    print(minus)
    print(plus)
    print(zero)

plusMinus(list(map(int, '-4 3 -9 0 4 1'.split())))