
def maximumMeetings(start,end):

    maxMeetings = 1

    time_list = [(i, j) for i, j in zip(start, end)]
    time_list = sorted(time_list, key=lambda x: x[1])

    prev_e = time_list[0][1]

    for index in range(1, len(time_list)):

        s = time_list[index][0]
        e = time_list[index][1]

        if s > prev_e:
            maxMeetings += 1
            prev_e = e

    return maxMeetings

print(maximumMeetings([10,12,20], [20,25,30]))