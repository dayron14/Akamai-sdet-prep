# Prompt:
# Write a function that takes a string and returns it reversed, without using [::-1] or reversed().
#
# Example:
#
# Input:  "Akamai"
# Output: "iamakA"

def reverse_string(string: str)-> str:
    reversed_string=''

    for char in string:
        reversed_string= char+reversed_string
    return reversed_string

print(reverse_string('Akamai'))
