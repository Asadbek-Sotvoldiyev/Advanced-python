class Solution(object):
    def isHappy(self, n):
        self.seen = set()

        while n!=1 and n not in self.seen:
            self.seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n==1


num = Solution()
print(num.isHappy(19))
# Result: True
