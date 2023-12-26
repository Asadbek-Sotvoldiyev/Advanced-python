def mydecorator(function):

    def wrapper(*args, **kwargs):
        print('I am decorating your function!')
        return function(*args, **kwargs)

    return wrapper

@mydecorator
def hello(person):
    return f'Hello {person}'

print(hello('Asadbek'))




