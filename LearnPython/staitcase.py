def staircase(n):
    print(('\n'.join([(i*str('#')).rjust(n) for i in range(1, n+1)])))

staircase(6)
