d = {"a": 1, "b": 2, "c": 3}

def invert_dict(d: dict):
    inverted_dict={}
    for key,value in d.items():
        inverted_dict[value]=key
    return inverted_dict

print(invert_dict({"a": 1, "b": 2, "c": 3}))
