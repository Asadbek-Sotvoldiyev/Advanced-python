def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

nums = [34,2,35,67,23]
bubble_sort(nums)
print(nums)
#Natija: [67, 35, 34, 23, 2]
