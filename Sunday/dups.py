# Example: [1, 2, 3, 1, 2, 4] → [1, 2]

def find_dups(dups_list:list) -> list:
    deduped_list=set()

    for item in dups_list:
        if dups_list.count(item)>1:
            deduped_list.add(item)
    return list(deduped_list)

print(find_dups([1, 2, 3, 1, 2, 4]))


