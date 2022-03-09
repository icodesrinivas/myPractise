
def repeatedString(s, n):
    print('s.count("a")', s.count('a'))
    print('s.count("a") * n // len(s))', s.count('a') * n // len(s))
    return (s.count('a') * (n // len(s))) + s[:n%len(s)].count('a')

print(repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570))
s = 'aab'
print(s[:(10%len(s))])
print(882787%3)

'aab'
882787
588525
