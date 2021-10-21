# Write a Python program that creates and displays a dictionary that maps each letter in a string to how many times the character occurs in the string (its frequency).
#
# The dictionary should only include the characters in the string.
#
# The test should be case-insensitive ("A" should be counted as "a").
#
# The keys in the dictionary should be lowercase letters.
#
# Only include letters in the dictionary.
#
# 🔹 Expected Output:
# Example 1:
# For the string:"Hello, World"
#
# The output should be this dictionary:
# {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
# Each letter is mapped to its corresponding frequency.
#
# Example 2: "Excellent"
# The output should be this dictionary:
# {"e": 3, "x": 1, "c": 1, "l": 2, "n": 1, "t": 1}

s = "hello, world"
a = {}
for i in s:
    if i.isalpha():
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
print(a)