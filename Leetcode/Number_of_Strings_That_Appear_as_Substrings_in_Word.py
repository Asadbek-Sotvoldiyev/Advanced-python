class Solution(object):
    def numOfStrings(self, patterns, word):
        self.n = 0
        for i in patterns:
            if i in word:
                self.n+=1
        return self.n

num0fString = Solution()
print(num0fString.numOfStrings(["a","abc","bc","d"], "abc"))
