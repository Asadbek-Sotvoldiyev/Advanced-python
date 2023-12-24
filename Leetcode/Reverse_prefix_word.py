class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            return "".join(word[:word.index(ch)+1][::-1])+"".join(word[word.index(ch)+1:])
        else:
            return word



word = Solution()
print(word.reversePrefix("abcdefd", "d"))
# Result: 'dcbaefd'
