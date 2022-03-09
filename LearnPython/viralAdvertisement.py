
def viralAdvertising(n):
    result = 0
    shared = 5
    for i in range(1,n+1):
        result += (shared // 2)
        shared = (shared // 2) * 3
    return result

print(viralAdvertising(5))

