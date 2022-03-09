obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

def collectStrings(obj):
    result = []
    for obj_key in obj:
        if type(obj[obj_key]) == str:
            result.append(obj[obj_key])
        else:
            return result + collectStrings(obj[obj_key])

    return result

print(collectStrings(obj))  # ['foo', 'bar', 'baz']

