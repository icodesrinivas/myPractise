#
#
import re
#
# string = '''
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# cerey-121-schafer@my-work.net
# '''
#
# url = '''
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov
# '''
#
# print(re.compile(r'.'))
# pattern = re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|edu|net)')

# pattern = re.compile((r'https?://(www\.)?[a-z]+\.(com|gov)'))
# matches = pattern.finditer(url)
#
# [print(match) for match in matches]
#
# string = '100,000,000.000'
#
# reg_pat = r"\d"
#
# print(reg_pat)
#
# print(re.split(r'[,.]', '100,000,000.000'))
# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')

# my_string = '..123456111aaa'
#
# matches = re.findall(r'((\w)\2{2,})', my_string)
# # re.findall(r'((\w)\2{2,})', my_string)
# print(matches[0][1])
# [print(matches[0][1]) if len(matches)>0 else -1]


# print(matches.group(1) if matches else -1)
# result = re.finditer(r'[.]*?1{2}', my_string)
# print(result)

import re
# string = 'abaabaabaazeebaae+-'
# # vowel AEIOU
# # consonants QWRTYPSDFGHJKLZXCVBNM
# # result = re.finditer(r'[^aeiuoAEIOU]([aeiuoAEIOU])\1+[^aeiuoAEIOU]', string)
# result = re.finditer(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiuo]{2,})+[qwrtypsdfghjklzxcvbnm]', string, flags=re.I)
#
# output = [x.group() for x in result]
# print(output)
#
# [print(x[0:len(x)-1]) for x in output]


# S = 'aabcdeffgabcdef'
# sub = 'abcdef'
#
# # result = re.search(r'%s' % (sub), S, flags=re.IGNORECASE)
# # print(result)
#
# output = []
# for item in range(len(S)):
#     result = re.search(r'%s' % (sub), S[item:item+len(sub)], flags=re.IGNORECASE)
#     if result != None:
#         output.append((int(result.start())+item, int(result.start())+item+(len(sub)-1)))
#
# if len(output) > 0:
#     [print(x) for x in output]
# else:
#     print((-1,-1))

print('&&' in '  &  ')

line = '#Note do not change && || & or |'
# print(line)
#
# print(re.sub(r'(?<= )(&&|\|\|)(?= )', 'and', line))
# print(re.sub(r'\|\|', 'or', line))

print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x:'and' if x.group() == '&&' else 'or', line))
print(re.sub(r'(?<= )(&&|\|\|)(?= )', 'and' if '&&' else 'or', line))
# print('#' in 'Note do not change && or ||| or & or |')