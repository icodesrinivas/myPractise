def print_rangoli(size):
    # your code goes here
    #
    # MY SOLUTION
    if size == 1:
        print('a')
    else:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        rangoli_alpha = alphabets[0:size][::-1]
        middle_pattern = '-'.join(rangoli_alpha) + '-' + '-'.join(rangoli_alpha[:-1])[::-1]
        upper_pattern = ''
        for item in range(1, size):
            if item == 1:
                upper_pattern += '-'.join(rangoli_alpha[:item]).center(len(middle_pattern), '-') + '\n'
            else:
                upper_pattern += (('-'.join(rangoli_alpha[:item]) + '-' + '-'.join(rangoli_alpha[:item-1][::-1])).center(len(middle_pattern), '-') + '\n')


        print(upper_pattern + middle_pattern + upper_pattern[::-1])

    # BEST SOLUTION
def print_rangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1] + items[::-1]
    for i in items:
        temp = data[-(i + 1):]
        row = temp[::-1] + temp[1:]
        print("-".join(row).center(n * 4 - 3, "-"))

if __name__ == '__main__':
    n = 2
    print_rangoli(n)