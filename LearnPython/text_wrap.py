def wrap(string, max_width):
    lis = [string[x:x+max_width] for x in range(0, len(string), max_width)]
    return '\n'.join([string[x:x+max_width] for x in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
    result = wrap(string, max_width)
    print(result)

for item in range(0, 26, 4):
    print(item)