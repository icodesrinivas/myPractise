# Given a list of meeting intervals, find the least number of meeting rooms required.

def meeting_rooms(A):

    if len(A) == 0:
        return 0

    data = []
    for s, e in A:
        data.append((s, 1))
        data.append((e, -1))

    data.sort()
    curr_room = 0
    max_room = 0

    for t, room in data:
        curr_room += room
        max_room = curr_room if curr_room >= max_room else max_room

    return max_room

print(meeting_rooms([[5,10], [15,20], [0,30]]))