obj2 = {
"num": 1,
"test": [1,2,3],
"data": {
    "val": 4,
    "info": {
        "isRight": True,
        "random": 66
    }
}
}

def stringifyNumbers(obj):

    for obj_key in obj:
        if type(obj[obj_key]) in [dict]:
            obj[obj_key] = stringifyNumbers(obj[obj_key])

        if type(obj[obj_key]) in [list]:
            if len(obj[obj_key]) > 0:
                obj[obj_key] = [str(i) for i in obj[obj_key]]

        if type(obj[obj_key]) == int:
            obj[obj_key] = str(obj[obj_key])


    return obj

print(stringifyNumbers(obj2))



