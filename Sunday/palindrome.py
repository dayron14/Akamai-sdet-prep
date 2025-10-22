def palindrome_checker() -> bool:
    stripped_word = input('Please enter a word to analyze:').lower().strip()
    return stripped_word==''.join(reversed(stripped_word))

print(palindrome_checker())