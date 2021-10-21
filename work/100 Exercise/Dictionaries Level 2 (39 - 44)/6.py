# Write a Python program that takes the content of a dictionary and converts it into a list of lists.
#
# Each nested list should contain a key as the first element and its corresponding value as the second element.
#
# Print the final list of lists.
#
# 🔹 Expected Output:
# If this is the original dictionary:
#
# product_info = {
# 	"description": "shoe",
# 	"price": 4.56,
# 	"colors": ["green", "blue", "red"],
# }
# The output should be:
#
# [['description', 'shoe'], ['price', 4.56], ['colors', ['green', 'blue', 'red']]]

a = {"description": "shoe", "price": 4.56," colors": ["green", "blue", "red"]}
b = []
for i in a.items():
    b.append(list(i))
print(b)

# ++++++++++++++++++++++++++ OR +++++++++++++++++++++++++++++++
c = []
for i,j in a.items():
    c.append([i, j])
print(c)





