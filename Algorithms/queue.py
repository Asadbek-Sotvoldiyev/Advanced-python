class MyQueue:
    queue = []
    def inqueue(self,a):
        self.queue.append(a)
    def dequeue(self):
        if self.queue:
            self.queue.remove(self.queue[0])
        else:
            raise ValueError('List ichida element mavjud emas')
    def peek(self):
        return self.queue[0]
    def isEmpty(self):
        if self.queue:
            return True
        else:
            return False
    def show(self):
        return self.queue

my_queue = MyQueue()
my_queue.inqueue(12)
my_queue.inqueue(43)
my_queue.inqueue(2)
my_queue.inqueue(4)
my_queue.inqueue(65)

print(my_queue.show())
# result: [12, 43, 2, 4, 65]
my_queue.dequeue()
print(my_queue.show())
# result: [43, 2, 4, 65]


