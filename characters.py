# Count characters
# Count how many times each character appears in a string and return a dictionary.
# Example: "edge" → {'e': 2, 'd': 1, 'g': 1}.

def char_counter(word) -> dict:
    freq ={}

    for char in word:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return  freq

print(char_counter('edge'))