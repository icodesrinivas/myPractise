

def beautifulDays(i, j, k):
    # return len([abs(day - int(str(day)[::-1])) for day in range(i, j+1) if abs(day - int(str(day)[::-1])) % k == 0])

    return len(list(filter(lambda x: abs(x - int(str(x)[::-1])) % k == 0, range(i, j+1))))
print(beautifulDays(20,23,6))

