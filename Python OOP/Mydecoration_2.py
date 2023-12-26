# Practical example 1 - Logging
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt','a+') as file:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            file.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x,y):
    return x+y

print(add(10,20))
print(add(40,89))

