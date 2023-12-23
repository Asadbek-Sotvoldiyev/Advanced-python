class Solution(object):
    def binary_search(self,arr,value):
        starts = 0
        ends = len(arr)

        while starts<=ends:
            mid_index = (starts+ends)//2
            if value==arr[mid_index]:
                return True
            elif arr[mid_index]>value:
                ends-=1
            else:
                starts+=1
        return False

    def intersection(self, nums1, nums2):
      self.n = []
      for i in nums2:
        if self.binary_search(nums1,i):
          self.n.append(i)
      return list(set(self.n))

nums1 = [1,2,2,1]
nums2 = [2,2]
a = Solution()
print(a.intersection(nums1, nums2))

# Natija: [2]


