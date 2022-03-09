# Enter your code here. Read input from STDIN. Print output to STDOUT

# s = 'qwerty123456789dfghj123456789QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
#
# s_dict = {'small': '', 'capital': '', 'digits': ''}
#
# for item in s:
#     if item.islower():
#         s_dict['small'] += item
#     elif item.isupper():
#         s_dict['capital'] += item
#     else:
#         s_dict['digits'] += item
#
# odd = []
# even = []
#
# for digit in s_dict['digits']:
#     if int(digit) % 2 == 0:
#         even.append(digit)
#     else:
#         odd.append(digit)
#
# s_dict['digits'] = ''.join(sorted(odd) + sorted(even))
#
# print(sorted(s_dict['small']))
# print(sorted(s_dict['capital']))
# print(s_dict['digits'])
#
# print(''.join(sorted(s_dict['small'])) + ''.join(sorted(s_dict['capital'])) + s_dict['digits'])

s = 'qwerty123456789dfghj123456789QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
# print(*sorted('qwerty123456789dfghj123456789QWERTYUIOPASDFGHJKLZXCVBNM0123456789', key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')
# print(-64 >> 5)

# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

#
# order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
# print(*sorted('qwerty123456789dfghj123456789QWERTYUIOPASDFGHJKLZXCVBNM0123456789', key=order.index), sep='')
#
import string
# print(*sorted(s, key=(string.ascii_letters + '1357902468').index), sep='')
# print(string.ascii_letters)
s = 'qwerty123456789dQWERTYUIOfghj123456789PASDFGHJKLZXCVBNM0123456789'
import re
alpha = ''.join(sorted(''.join(re.findall(r'[a-z]*', s))))
print(alpha)
digit = re.findall(r'[02468]*', s)
odd = ''.join(sorted(re.findall(r'[13579]', s)))
print(odd)
print("+++++++++++++++++")
print(*sorted(s, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

print(chr(65))