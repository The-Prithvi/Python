import time

def srch():
    book = " coroutines are similar to generators but with few e" \
           "xtra methods and slight changes in how we use yield " \
           "statements. Generators produce data for iteration while" \
           " coroutines can also consume data."
    time.sleep(2)

    while True:
        text = (yield )
        if text in book:
            print("Present")
        else:
            print("Not Present")

search = srch()
next(search)
search.send("generators")
input("Press Any key To Contnue")
search.send("data")