
def dec_to_bin(n):
    if n//2 == 0:
        return n%2
    else:
        return str(n%2) + str(dec_to_bin(n//2))

print(dec_to_bin(134))

# 13/2 6 1
# 6/2 3 0
# 3/2 1 1
# 1/2 0 1