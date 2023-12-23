def binary_search(arr,value):
    starts = 0
    ends = len(arr)-1

    while starts<=ends:
        mid_index = (starts+ends)//2
        if value==arr[mid_index]:
            return True
        elif arr[mid_index]>value:
            ends-=1
        else:
            starts+=1
    return False

print(binary_search([1,2,3,4,5,6,7,8], 7))
# Natija: 6
