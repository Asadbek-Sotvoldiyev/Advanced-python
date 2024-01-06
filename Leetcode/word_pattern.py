class Solution(object):
    def wordPattern(self, pattern, s):
        pattern_list = list(pattern)
        s_list = s.split()
        n = 0
        for i in pattern_list:
            if i=='a' and s_list[n]=='dog':
                n+=1
            elif i=='b' and s_list[n]=='cat':
                n+=1
        return True if n==len(s_list) else False

a = Solution()
print(a.wordPattern("abba","dog cat cat fish"))


