# Remove all vowels from a string.
def vowel_remover(word):

    vowels=['a','e','i','o','u']
    result=""

    for char in word:
        if char not in vowels:
            result+=char
    return result
print(vowel_remover('banana'))