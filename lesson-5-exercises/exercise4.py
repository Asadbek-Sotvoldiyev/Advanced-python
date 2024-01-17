def func(arr):
    n = range(min(arr), max(arr)+1)
    for i in n:
        if i not in arr:
            return i
print(func([3,0,1,4,2,6]))
# result: 5