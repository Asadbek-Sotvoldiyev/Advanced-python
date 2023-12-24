class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    def __next__(self):
        if self.start>=self.end:
            raise StopIteration
        count = self.start
        self.start+=1

        return count

nums = MyRange(1,10)
for i in nums:
    print(i)
