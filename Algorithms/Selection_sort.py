def selection_sort(arr):
    if len(arr)<2:
        return arr
    else:
        minElement = min(arr)
        array = list(filter(lambda x: x!=minElement, arr))
        return [minElement] + selection_sort(array)

print(selection_sort([98,6,45,2,4,5,12,23,11]))
