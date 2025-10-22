# Example: ["bat","tab","tap","pat","cat"] → [["bat","tab"],["tap","pat"],["cat"]]

def anagram_grouper(ana_list:list) -> list:
    grouped_anagrams={}
    for word in ana_list:
        key = ''.join(sorted(word))
        # print(grouped_anagrams.keys())
        if key not in grouped_anagrams:
            grouped_anagrams[key]=[]
        grouped_anagrams[key].append(word)
    return list(grouped_anagrams.values())

print(anagram_grouper(["bat","tab","tap","pat","cat"]))





