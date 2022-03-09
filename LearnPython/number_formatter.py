def print_formatted(number):
    # your code goes here
    for item in range(number):
        print('\s+'.join([str(item), oct(item)[2:], hex(item)[2:].upper(), bin(item)[2:]]))

if __name__ == '__main__':
    n = 5
    # print_formatted(n)

    # width = ("{0:b}".format(4))
    # print(width)

    # print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(1, width=3))
    # # print("{k:.3f}".format(k=20))
    # print("{k:{c}{o}}".format(k=20, c=2, o='f'))
    #
    # print(len("{0:b}".format(2)))
    # print("{0:{w}d}".format(1, w=2))
    print(int('{0:1b}'.format(120), 16))
