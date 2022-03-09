import itertools

def getTotalX(a, b):

    nbc = [x for x in range(a[-1], b[0]+1) if x%a[-1]==0]
    print('nbc=', nbc)
    print('a=', a)
    print('b=', b)

    print('++++++++++++++++')
    print()

    k = list(filter(lambda x: x if all([x%y==0 for y in a]) else '', nbc))
    print(k)

    p = list(filter(lambda x: x if all([y%x==0 for y in b]) else '', k))
    print(p)

    3
    line
    solution in python

    ```

    def getTotalX(a, b):
        # Find numbers to be considered
        nbc = [x for x in range(a[-1], b[0] + 1) if x % a[-1] == 0]

        # Apply filter on numbers to be considered (nbc) to check if all the elements of 'a' are factor of elements of nbc.
        k = list(filter(lambda x: x if all([x % y == 0 for y in a]) else '', nbc))

        # Finally apply filter to 'k' to check if elements of 'k' are factors of 'b'
        return len(list(filter(lambda x: x if all([y % x == 0 for y in b]) else '', k)))

    ```





    # print(a_fac)

getTotalX([2, 4], [16, 32, 96])