def breakingRecords(scores):
    print(scores)
    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0
    for index in range(1, len(scores)):

        if scores[index] == max_score:
            continue

        if scores[index] > max_score:
            max_score = scores[index]
            max_count += 1
        elif scores[index] < min_score:
            min_score = scores[index]
            min_count += 1


    print([max_count, min_count])
    return [max_count, min_count]

breakingRecords(list(map(int, '10 5 20 20 4 5 2 25 1'.split(' '))))