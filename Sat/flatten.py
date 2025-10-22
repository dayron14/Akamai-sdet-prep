# Flatten a nested list (e.g., [[1,2],[3,4],[5]] → [1,2,3,4,5]).
def flatten_nested(unflattened_list: list) -> list:
    flat_list=[]
    for sublist in unflattened_list:
        for item in sublist:
            flat_list.append(item)
    return  flat_list

print(flatten_nested( [[1,2],[3,4],[5]]))
#
# Rotate a list k steps to the right (e.g., [1,2,3,4,5], k=2 → [4,5,1,2,3]).

