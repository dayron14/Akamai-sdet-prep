# Example: ["bat","tab","tap","pat","cat"] → [["bat","tab"],["tap","pat"],["cat"]]


def an_grouper(anagram_list:list)->list:
    anagram_dict={}
    for anagram in anagram_list:
        key=''.join(sorted(anagram))
        if key not in anagram_dict:
            anagram_dict[key]=[]
        anagram_dict[key].append(anagram)
    return list(anagram_dict.values())

print(an_grouper(["bat","tab","tap","pat","cat"] ))




