obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {
            "superInner": 2,
            "notANumber": True,
            "alsoNotANumber": "yup"
        }
    }
}

obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": 'car'}
}


def nestedEvenSum(obj, sum=0):

    for obj_key in obj.keys():
        if type(obj[obj_key]) == dict:
            sum = nestedEvenSum(obj[obj_key], sum)
        else:
            if type(obj[obj_key]) == int and obj[obj_key] % 2 == 0:
                sum += obj[obj_key]
    return sum

print(nestedEvenSum(obj2, 0))

# b = {"a": {"c": 3, "d": 2}}
# print(type(b))
# print(type(b.values()))