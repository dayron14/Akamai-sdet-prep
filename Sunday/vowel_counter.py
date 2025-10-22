# "akamai" → {'a': 3, 'k': 1, 'm': 1, 'i': 1}

def vowel_counter(word) -> dict:
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_dict = {}

    for letter in word:
        if letter in vowels:
            if letter in vowel_dict:
                vowel_dict[letter] += 1
            else:
                vowel_dict[letter] = 1
    return vowel_dict


print(vowel_counter('akamai'))
