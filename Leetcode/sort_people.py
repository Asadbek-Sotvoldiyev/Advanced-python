class Solution(object):
    def sortPeople(self, names, heights):
        peoples = {heights[i]:names[i] for i in range(len(names))}
        return [peoples[i] for i in sorted(heights)[::-1]]


people = Solution()
print(people.sortPeople(["Alice","Bob","Bob"], [155,185,150]))
