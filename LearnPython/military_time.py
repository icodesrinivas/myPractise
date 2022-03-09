def timeConversion(s):
    AMPM = s[len(s)-2:len(s)]
    time = s[:len(s)-2].split(':')
    # print(time[0])
    if AMPM == 'AM':
        return ':'.join(['00' if time[0] == '12' else time[0] for _ in [time[0]]] + time[1:])
    else:
        return ':'.join([str(int(time[0]) + 12) if time[0] != '12' else time[0] for _ in [time[0]]] + time[1:])

    # ['00' if time[0] == '12' else time for _ in time]


print(timeConversion('01:05:45PM'))