def quick_upsort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr.pop()
        start_list = list(filter(lambda x: x<pivot, arr))
        end_list = list(filter(lambda x: x>pivot, arr))
        return quick_upsort(end_list) + [pivot] + quick_upsort(start_list)
def reverse_num(num):
    num_list = list(map(int, list(str(num))))
    res = list(map(str, quick_upsort(num_list)))
    return "".join(res)

def reverse_arr(nums):
    for i in range(len(nums)):
        nums[i] = reverse_num(nums[i])
    return nums
print(reverse_arr([459, 69, 85, 213]))
# result: ['954', '96', '85', '321']

