def are_we_anagrams(w1: str, w2: str) -> bool:
    w1_list=sorted(list(w1.lower().replace(' ','')))
    w2_list=sorted(list(w2.lower().replace(' ','')))

    return  w1_list==w2_list



if __name__ == "__main__":
    word1 = input('Enter the first word: ')
    word2 = input('Enter the second word: ')
    if are_we_anagrams(word1, word2):
        print('The words are anagrams')
    else:
        print('Nope')