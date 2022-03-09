def pairSum(myList, sum):
    output = []
    for index in range(len(myList)):
        rem = sum - myList[index]
        if rem in myList[index+1:]:
            output.append(f'{myList[index]}+{rem}')

    return output
print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
print(id1)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id2)
print(id1 == id2)


init_tuple_a = 1, 2
init_tuple_b = (3, 4)
print([init_tuple_a + init_tuple_b])
[print(x) for x in [init_tuple_a + init_tuple_b]]
[print(y) for y in [1,2,3,4]]