class Solution(object):
    def shuffle(self, nums, n):
        return [x for pair in zip(nums[:n], nums[n:]) for x in pair]

a = Solution()
print(a.shuffle([2,5,1,3,4,7],3))
