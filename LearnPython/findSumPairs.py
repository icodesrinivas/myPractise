
arr = [2,4,6,0,3,3,9,-11,17]
target = 6
result = []
def findSumPairs(arr, target):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i]+arr[j] == target and arr[i] != arr[j] and (arr[j], arr[i]) not in result:
                result.append((arr[i],arr[j]))
    return result

print(findSumPairs(arr, target))