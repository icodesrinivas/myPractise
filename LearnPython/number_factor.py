# sum_list = [1,3,4]
# N = 4

def number_factor(N):
    if N in [0,1,2]:
        return 1
    if N == 3:
        return 2
    print('N', N)
    subP1 = number_factor(N-1)
    print('subP1',subP1)
    subP2 = number_factor(N-3)
    print('subP2', subP2)
    subP3 = number_factor(N-4)
    print('subP3', subP3)
    return subP1 + subP2 + subP3


print(number_factor(5))