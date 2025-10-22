# 2️⃣ Key existence check
# Task: Write a function that takes a dictionary and a key, and returns:
# "Found" if it exists
# "Not found" otherwise
# Example:
# check_key({'a': 1, 'b': 2}, 'b')  # → "Found"
# check_key({'a': 1, 'b': 2}, 'z')  # → "Not found"

def check_key(dict1: dict, key ):
        if key in dict1:
            print('Found')
        else:
            print('not found')

check_key({'a': 1, 'b': 2}, 'b')
