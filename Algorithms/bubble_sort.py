def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def rever(arr):
    a = list(map(str, arr))
    b = list(map(lambda x: x[::-1] if len(x)>=2 else x, a))
    return list(map(int, bubble_sort((b))))

# print(rever([34,2,35,67,23]))
#out: [2,32,43,53,76]

