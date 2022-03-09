def saveThePrisoner(n, m, s):
    if abs(n - s) >= m:
        return abs(s+m)-1
    else:
        rem_m = m - (abs(s-n)+1)
        k = n if rem_m % n ==0 else rem_m % n
        return n - (n - k)

print(saveThePrisoner(7,19,2))