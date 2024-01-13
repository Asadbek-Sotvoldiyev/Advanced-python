def add_function(arr1, arr2):
    res = ""
    for i in range(min(len(arr1), len(arr2))):
        res += str(arr1[i]+arr2[i])
    return int(res)

print(add_function([1,1,1], [2,2,2]))
# result: 33