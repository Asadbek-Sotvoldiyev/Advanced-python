def func(arr):
    for i in arr:
        if arr.count(i)==1:
            return i

print(func([2,2,1,4,5,4,5,8,7,7,8]))