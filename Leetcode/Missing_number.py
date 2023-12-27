class Solution(object):
    def missingNumber(self, nums):
        self.full_nums = range(min(nums),max(nums)+1)
        self.num =  [i for i in self.full_nums if i not in nums]
        if self.num:
            return self.num[0]
        elif 0 not in nums:
            return 0
        else:
            return len(nums)

missing_nums = Solution()
print(missing_nums.missingNumber([9,6,4,2,3,5,7,0,1]))
# Result: 8
