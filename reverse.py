def reverse(s):
    return s[::-1]

print(reverse('Akamai'))

def anotherway(word):
    reversed_word=''
    for char in word:
        reversed_word=char + reversed_word
    return reversed_word

print(anotherway('Akamai'))

def antherone(new):
    return  ''.join(reversed(new))

print(anotherway('Akamai'))