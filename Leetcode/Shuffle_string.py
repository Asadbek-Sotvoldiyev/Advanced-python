class Solution(object):
    def restoreString(self, s, indices):
        self.a = {}
        for i in range(len(s)):
            self.a[indices[i]]=s[i]
        self.b = []
        for i in sorted(indices):
            self.b.append(self.a[i])
        return "".join(self.b)
