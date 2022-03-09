
from collections import Counter
room_list = list(map(int, '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'.split(' ')))
# print(len(room_list))
# print(set(room_list))
# print(((sum(set(room_list))*5)-(sum(room_list)))//(5-1))
# print(Counter(room_list))
# room_list = Counter(room_list)

# [print(key) for key,value in room_list.items() if value == 1]
# print(result)

k, rooms, single, multiple = 5, room_list, set(), set()
for room in rooms:
    if room not in single:
        single.add(room)
    else:
        multiple.add(room)
print(single.difference(multiple).pop())