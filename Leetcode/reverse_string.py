class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)):
            b = s.pop()
            s.insert(i,b)
        return s

a = Solution()
print(a.reverseString(["h","e","l","l","o"]))
