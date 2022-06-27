

def f(n):

    if n == 1:
        print('***********')
    print("n ",n)
    for i in range(n): 
        f(n-1)

f(3)