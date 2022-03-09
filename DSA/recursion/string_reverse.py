
def reverse(string):
    n = len(string)
    if n == 1:
        return string[0]
    else:
        return string[-1] + reverse(string[:n-1])

print(reverse('python'))