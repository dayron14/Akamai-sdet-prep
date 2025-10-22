

#first approach
def is_palindrome(word):
    return word==''.join(reversed(word))

print(is_palindrome('mom'))

#second approach

def another_approach(word):
    reversed_word=''
    for character in word:
        reversed_word=character+reversed_word
    if word ==reversed_word:
        print('it is a palindrome')

print(another_approach('mom'))

# Find duplicates in a list
# Given [1,2,3,1,2,4], return [1,2].

def find_dups(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if  number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    return  list(duplicates)

print(find_dups([1,2,3,1,2,4]))


# Sum of even numbers
# Given a list of integers, return the sum of all even numbers.

def sum_of_evens(numbers: list) -> int:

    evens=list()
    for number in numbers:
        if number%2==0:
            evens.append(number)
    return sum(evens)

print(sum_of_evens([1,1,2,2,2,3,4,5]))

