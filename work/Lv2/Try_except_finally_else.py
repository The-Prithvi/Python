try:
    # print(x)
    print("Hello")
except Exception as e:
    print(e)

# The finally block, if specified, will be executed regardless if the try block raises an error or not
# finally:
#     print("The 'try except' is finished")

# You can use the else keyword to define a block of code to be executed if no errors were raised
else:
    print("Else block excecuted")

print("Important code: ")