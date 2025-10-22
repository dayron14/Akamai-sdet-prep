# 6️⃣ First non-repeating character
#  "swiss" → "w"

def repeated_chars(word):
    for char in word:
        if word.count(char)==1:
         return char

print(repeated_chars('aahhjjlaa'))




# 7️⃣ Flatten a nested list
#  [1, [2, [3, 4]], 5] → [1, 2, 3, 4, 5]

# 8️⃣ Merge two dictionaries
#  {'a':1,'b':2} + {'a':3,'c':5} → {'a':4,'b':2,'c':5}



# 9️⃣ Remove keys with None values
#  {'a':1, 'b':None, 'c':3} → {'a':1,'c':3}


# 🔟 Validate balanced parentheses
#  "({[]})" → True, "([)]" → False

def is_anagram(word1,word2) -> bool:
    return  sorted(list(word1))== sorted(list(word2))

w1=input("enter the first word to analyze:")
w2=input("enter the second word to analyze:")


print(is_anagram(w1,w2))
