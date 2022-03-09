def fibonacci(n):

    lis = list(range(n))

    fibonacci_list = [0,1]

    # [fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2]) for i in list(range(n))[2:]]

    list(map(lambda i: fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2]), list(range(n))[2:]))

    print(fibonacci_list)



fibonacci(15)
