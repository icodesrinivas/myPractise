import numpy
n, m, p = '0 0 0'.split()
n, m, p = int(n), int(m), int(p)
zero_list = []
one_list = []
for _ in range(n):
    zero_list.append(numpy.zeros((m, p), dtype=int))
    one_list.append(numpy.ones((m, p), dtype=int))

print(numpy.concatenate([zero_list], axis=0))
print(numpy.concatenate([one_list], axis=0))