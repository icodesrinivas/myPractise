

arr = [1,2,3,4,5]

max_cal = sum(arr[0:arr.index(min(arr))]) + sum(arr[arr.index(min(arr))+1:])
min_cal = sum(arr[0:arr.index(max(arr))]) + sum(arr[arr.index(max(arr))+1:])

print(max_cal)
print(min_cal)