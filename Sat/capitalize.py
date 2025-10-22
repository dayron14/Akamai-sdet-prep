# Write a function that capitalizes the first letter of each word in a sentence (without using .title()).

def capitalize(sentence: str):
    word_list=sentence.split()
    capitalized_words=[]

    for word in word_list:
        capitalized_word=word[0].upper()+word[1:]
        capitalized_words.append(capitalized_word)

    return ' '.join(capitalized_words)

print(capitalize('this is all lower case'))