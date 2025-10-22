# Input:  "This is a test. This test is only a test."
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}

def frequency_of_words(sentence: str) -> dict:
    list_of_words=sentence.split()
    print(list_of_words)
    word_dict={}

    for word in list_of_words:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    return  word_dict

print(frequency_of_words('This is a test. This test is only a test.'))
