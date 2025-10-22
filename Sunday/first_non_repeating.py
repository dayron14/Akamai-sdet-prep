# Example: "swiss" → "w"
def find_non_repeating(string_to_analyze: str) -> str:

    stripped_word=string_to_analyze.lower().strip()
    non_repeating=[]

    for char in stripped_word:
        if stripped_word.count(char)==1:
            non_repeating.append(char)
    return non_repeating[0]

print(find_non_repeating('swiss'))