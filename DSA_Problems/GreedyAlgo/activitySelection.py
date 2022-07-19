# Activity Selection Problem
# Problem similar to maximum disjoint set problem


def maxActivity(start, finish):

    time_list = [(i, j) for i, j in list(zip(start,finish))]

    time_list = sorted(time_list, key=lambda x: x[1])

    prev_e = None

    max_activity = 0

    for s, e in time_list:
        print('s',s,'e',e)
        if not prev_e or s > prev_e:
            max_activity += 1
            prev_e = e

    return max_activity




print(maxActivity([5, 3], [7, 5]))