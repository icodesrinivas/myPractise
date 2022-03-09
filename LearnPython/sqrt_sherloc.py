import math
# print(math.sqrt(10)%1==0)

result = 0
# print([1 for i in range(2,10+1) if math.sqrt(i)%1==0])
# print(filter(lambda x: math.sqrt(x)%1 == 0, range(2, 10+1)))
# print(len(list(filter(lambda x: math.sqrt(x)%1 == 0, range(17, 24+1)))))

# print([x for x in range(2, 10+1) if math.sqrt(x)%1 == 0])

print(math.sqrt(2))
print(math.sqrt(17))

a_sqrt = int(str(math.sqrt(4)).split('.')[0]) if math.sqrt(4)%1==0 else int(str(math.sqrt(4)).split('.')[0]) + 1
b_sqrt = int(str(math.sqrt(17)).split('.')[0])

print(a_sqrt)
print(b_sqrt)

print(len(range(2,4+1)))

