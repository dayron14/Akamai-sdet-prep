# Merge two lists and keep only common elements.

def common_el(list1 : list, list2: list):

    only_common=[]

    for element in list1:
        if element in list2 and element not in only_common:
            only_common.append(element)
    return only_common

print(common_el([1,1,2,3,4,4,4,5],[1,2,3,4,5,6]))
