# Count the frequency of each character in a string.
def frequency(word: str):
    freq={}
    stripped_word=word.lower()
    for char in stripped_word:
        if char in freq:
            freq[char] +=1
        else:
             freq[char]=1
    return freq

print(frequency('Akamai'))

# Example: "edge" → {'e': 2, 'd': 1, 'g': 1}
def char_counter(sentence: str) -> dict:
    freq={}
    stripped_sentence=sentence.lower()
    for char in stripped_sentence:
        if char in freq:
            freq[char]=+1
        else:
            freq[char]=1
    return freq

print(char_counter('Akamai'))