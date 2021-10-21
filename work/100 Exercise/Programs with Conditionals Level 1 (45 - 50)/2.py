# Write a Python program that prints a descriptive message indicating if each character in a string is a vowel or a consonant. For example: "<char> is a <consonant | vowel>"
#
# If the character is a special character, number, or symbol, print "<char> is not a letter".
#
# If the string is empty, print "Empty String".
#
# 🔹 Expected Output:
# If the string is:
#
# "Score: 36"
#
# The expected output would be:
#
# s is a consonant
# c is a consonant
# o is a vowel
# r is a consonant
# e is a vowel
# : is not a letter
#   is not a letter
# 3 is not a letter
# 6 is not a letter
s = "Score : 36"
v = ["a", "e", "i", "o", "u"]
if not s:
    print("Empty String")
else:
    for i in s.lower():
        if i in v:
            print(str(i) + ": Vowel")
        elif not i.isalpha():
            print(str(i) + ": Not A Letter")
        else:
            print(str(i) + ": Letter")
