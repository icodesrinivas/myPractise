N = 9
M = 27

pattern = '.|.'
for row_count in range(1,N,2):
    print((pattern*row_count).center(M, '-'))
print('WELCOME'.center(M, '-'))
for row_count in range(N-2, 0, -2):
    print((pattern*row_count).center(M, '-'))

print("&&&&&&&&&&&&&&&&&")

pattern = '\n'.join([((pattern*i)).center(M, '-') for i in range(1,N,2)])
print(pattern)
print(pattern[::-1])

