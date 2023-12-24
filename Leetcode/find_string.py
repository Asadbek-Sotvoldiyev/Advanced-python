class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        self.n = 0
        self.index = 0
        for i in words:
            self.index = words.index(i)
            words.remove(i)
            if i[::-1] in words:
                self.n+=1
            words.insert(self.index, i)
        return self.n//2

words = Solution()
print(words.maximumNumberOfStringPairs(["ab","ba","cc"]))
# Result: 1
