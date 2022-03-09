from collections import Counter

candles = list(map(int, '3 2 1 3'.split()))

print(candles.count(max(candles)))

# arr = Counter(arr)

# print(arr)
# print(max(Counter(arr).keys()))
# print(arr[max(Counter(arr).keys())])

# candles = Counter(candles)
# candles[max(Counter(candles).keys())]