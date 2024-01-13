#Practical example 2 - Timing
import threading

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} funksiyasining bajarilish vaqti: {after-before}")
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result*=i
    return result

myfunction(90000)
#result: 3.8576242923736572
