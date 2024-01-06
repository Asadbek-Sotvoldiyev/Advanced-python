class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])



words = Solution()
print(words.reverseWords("the sky is blue"))
