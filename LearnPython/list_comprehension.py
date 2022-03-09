x = 1
y = 1
z = 1
n = 2

# result = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             print(i,j,k)
#             if sum([i,j,k]) != n:
#                 result.append([i,j,k])

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n])
