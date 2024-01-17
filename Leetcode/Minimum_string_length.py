class Solution(object):
    def minimizedStringLength(self, s):
        return len(list(set(list(s))))

a = Solution()
print(a.minimizedStringLength("aaabc"))

