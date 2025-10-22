def flatten_nested(nested_list: list) -> list:
    new_list=[]
    for list1 in nested_list:
        for sub_list in list1:
            new_list.append(sub_list)
    return new_list

print(flatten_nested([1, [2, [3, 4]], 5]))

