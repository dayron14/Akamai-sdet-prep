def string_reverser(string: str) -> str:
    return ''.join(reversed(string))

def another_way(string: str) -> str:
    return string[::-1]

word='hello'

print(''.join(reversed(word)))
print(string_reverser('Akamai'))
print(another_way('Akamai'))