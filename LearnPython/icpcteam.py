

a = {0,2,4}
b = {0,1,3}

# print(len(a.union(b)))

def acmTeam(topic):
    max_topics = 0
    max_teams = 0

    for i in range(len(topic)):
        i_topics = {x for x in range(len(topic[i])) if topic[i][x] == '1'}
        for j in range(i+1, len(topic)):
            j_topics = {y for y in range(len(topic[j])) if topic[j][y] == '1'}
            len_topics = len(i_topics.union(j_topics))
            if len_topics > max_topics:
                max_topics = len(i_topics.union(j_topics))
                max_teams = 1
            elif len_topics == max_topics:
                max_teams += 1


    return [max_topics, max_teams]

topics = ['10101','11100','11010','00101']
# print(int(topics[0]))

print(int('111111', 2))
print(bin(63 & 11))
# for i in range(len(topics)-1):
#     for j in range(i+1, len(topics)):
#         # print('topics[i]', topics[i], 'topics[j]', topics[j])
#         print('int(topics[i], 2)',int(topics[i],2))
#         print('int(topics[j], 2)',int(topics[j], 2))
#         result = bin(int(topics[i], 2) | int(topics[j], 2))
#         print(result)

# print(result)
# for i in topics:
#     print(int(i, base=2))
# print(acmTeam(topics))

# l = '10101'
# m = '11010'
# print(l | m)
# result = l.intersection(m)
# print(result)