
from collections import Counter
color = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 0
print((sum([(n+(x//2)) for x in Counter(color).values()])))
