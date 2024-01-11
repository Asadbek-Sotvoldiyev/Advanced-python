class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1 = list(map(str, l1))
        l2 = list(map(str, l2))
        res = str(int("".join(l1))+int("".join(l2)))
        return list(map(int, list((res)[::-1])))

a = Solution()
print(a.addTwoNumbers([2,4,3], [5,6,4]))