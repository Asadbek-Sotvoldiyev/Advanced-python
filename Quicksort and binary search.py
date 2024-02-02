def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr.pop()
        start_arr = list(filter(lambda x: x<pivot, arr))
        end_arr = list(filter(lambda x: x>pivot, arr))
        return quicksort(start_arr) + [pivot] + quicksort(end_arr)
    
a = [17, 18, 19,14, 15, 16, 20,10, 11, 12, 13,0, 1, 2, 3, 4, 5, 6,7, 8]
b = quicksort(a)
def binary_search(arr):
    start_index = 0
    end_index = len(b)-1
    while start_index<=end_index:
        mid_index = (start_index+end_index)//2
        if mid_index==b[mid_index] and mid_index+1!=b[mid_index+1]:
            return mid_index+1
        if mid_index==b[mid_index]:
            start_index = mid_index
        else:
            end_index = mid_index

print(binary_search(b))