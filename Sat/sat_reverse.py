def reverse(word):
    new_word= ''
    for char in word:
        new_word=char+new_word
    return  new_word

print(reverse('hello'))