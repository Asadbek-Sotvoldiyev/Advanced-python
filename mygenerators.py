def mygenerators(x):
        for i in range(x):
            yield i

values = mygenerators(10)
print(next(values))
print(next(values))
print(next(values))
print(next(values))



