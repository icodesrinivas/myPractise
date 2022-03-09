

s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
eval('s.pop()')
print(s)
# print(sum(s))
# print(s)
# s.pop()
# print(s)

# My Solution
# n = int(input())
# s = set(map(int, input().split()))
#
# for item in range(int(input())):
#     command = input().split()
#     if 'pop' in command:
#         s.pop()
#     elif 'remove' in command:
#         try:
#             s.remove(int(command[1]))
#         except:
#             pass
#     else:
#         s.discard(int(command[1]))

# print(sum(s))
#
# # Best solution 1
# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split()+['']))
#
# print(sum(s))
#
# # Best solution 2
# n = int(input())
# s = set(map(int, input().split()))
# d = {"pop":s.pop, "remove":s.remove, "discard": s.discard}
# for _ in range(int(input())):
#     c = input().split()
#     d[c[0]](int(c[1])) if len(c)>1 else d[c[0]]()
# print(sum(s))

