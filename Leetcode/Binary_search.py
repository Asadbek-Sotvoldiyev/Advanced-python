class Solution(object):
    def search(self, nums, target):
        start_index = 0
        end_index = len(nums)-1

        while start_index<=end_index:
          middle_index = (start_index+end_index)//2
          if nums[middle_index]==target:
            return middle_index
          elif nums[middle_index]>target:
            end_index-=1
          else:
            start_index+=1
        return -1

a = Solution()
print(a.search([-1,0,3,5,9,12], 9))