class Solution(object):
    def finalString(self, s):
        self.n = ""
        self.index = 0
        for i in s:
            if i=="i":
                self.n = self.n[::-1]
                continue
            else:
                self.n+=i

        return self.n

word = Solution()
print(word.finalString("string"))
# Result: 'rtsng
