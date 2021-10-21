import time
from functools import lru_cache


lru_cache(maxsize = 2)
def myfunc(x):
    time.sleep(2)
    print(x)


# myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
myfunc(1)
myfunc(2)
myfunc(3)
myfunc(4)
myfunc(5)
myfunc(6)
myfunc(7)
