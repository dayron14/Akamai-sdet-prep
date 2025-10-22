#
# FizzBuzz: Print numbers 1–100 with “Fizz” for multiples of 3, “Buzz” for 5, “FizzBuzz” for both.
# def fizz_buzz():
#     for i in range(1,100):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 5 == 0:
#             print("Buzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         else:
#             print(i)
# fizz_buzz()
# Write a function to check if a number is prime.
# def is_it_prime(number):
#     for i in range(number):
#         if i%1==0 and number%i==0:
#             print("the number is prime")
#         else:
#             print("the number is not prime")
#
# is_it_prime(4)
# Generate the first n Fibonacci numbers.
#
# Find all pairs in a list that sum to a target value.
#
# Detect if a string is a palindrome.

def is_it_palindrome(string : str) -> bool:
    stripped_string=string.replace(" ","").lower()
    reversed_string=''.join(reversed(stripped_string))
    print(stripped_string)
    return  stripped_string==reversed_string

print(is_it_palindrome('Race car'))
