def superReducedString(s):
    duplicate_exists = True
    while duplicate_exists:

        i = 0
        result = []
        count = 0
        while i < len(s):
            if i == len(s) - 1:
                result.append(s[i])
                i += 1
            else:
                if s[i] == s[i+1]:
                    count += 1
                    i += 2
                else:
                    result.append(s[i])
                    i += 1
        if count > 0:
            duplicate_exists = True
        else:
            duplicate_exists = False

        s = ''.join(result)
    return s if s != '' else 'Empty String'

print(len('aaabccddda'))
print(superReducedString('zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'))
print(superReducedString('aaabccddd'))
print(superReducedString('baab'))
'aaabccddd'
print(set('aa'))




print(''.join(set('aaabccddda')))