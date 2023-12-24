class Solution(object):
    def makeSmallestPalindrome(self, s):
        s = list(s)
        self.i,self.j = 0,len(s)-1

        while self.i<self.j:
            if s[self.i]!=s[self.j]:
                s[self.i] = s[self.j] = min(s[self.i], s[self.j])
            self.i += 1
            self.j -= 1

        return ''.join(s)
makePalindrome = Solution()
print(makePalindrome.makeSmallestPalindrome("egcfe"))
