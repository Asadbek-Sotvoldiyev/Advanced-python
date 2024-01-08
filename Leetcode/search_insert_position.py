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
class Solution(object):
    def searchInsert(self, nums, target):
        if binary_search(nums,target):
            return nums.index(target)
        else:
            for i in nums:
                if target<=i:
                    return nums.index(i)
            if target>max(nums):
                return nums.index(max(nums))+1


a = Solution()
print(a.searchInsert([1,3,5,6], 7))
