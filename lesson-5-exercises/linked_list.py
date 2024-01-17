class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def push(self,data):
        new_data = Node(data)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_data
    def show(self):
        current = self.head
        while current.next!=None:
            current = current.next
            print(current.data)
    def len(self):
        count = 0
        current = self.head
        while current.next!=None:
            current = current.next
            count+=1
        return count
    def remove(self, key):
        temp = self.head

        if temp is not None:
            self.head = temp.next
            temp = None
            return
        while temp is not None:
            if temp.data==key:
                break
            prev = temp
            temp = temp.next
        if temp==None:
            return
        prev.next = temp.next
        temp = None


my_list = LinkedList()
my_list.push('Asadbek')
my_list.push('Yahyobek')
my_list.push('Azizbek')
my_list.remove('Asadbek')
my_list.show()