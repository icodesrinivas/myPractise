def armstrongNumber (n):
    sum = 0
    for ele in str(n):
        print(ele)
        sum += int(ele)**3
        print(int(ele)**3)
    if sum == n:
        print(sum)
        return "Yes"

x = armstrongNumber(273)
print(x)

