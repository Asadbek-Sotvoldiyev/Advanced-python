from random import randrange
def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        a = arr.pop(randrange(len(arr)))
        starts_arr = list(filter(lambda x: x<a, arr))
        ends_arr = list(filter(lambda x: x>a, arr))
        return quick_sort(starts_arr) + [a] + quick_sort(ends_arr)

print(quick_sort([3,2,6,2,23,4]))
# return: [2, 3, 4, 6, 23]
