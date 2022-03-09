def migratoryBirds(arr):
    birds = {}
    for bird in arr:
        if bird in birds.keys():
            arr[bird] += 1
        else:
            arr[bird] = 1


s = {'a':2, 'b':4, 'c':4}

lis = [x for x,y in s.items() if y == max(s.values())]
print(lis)

