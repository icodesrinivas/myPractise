import re

N = int(input())

for _ in range(N):
    print('YES') if re.match(r'^(9|8|7)[0-9]{9}$', input()) else print('NO')