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

my_list = LinkedList()
my_list.push('Asadbek')
my_list.push('Yahyobek')
my_list.push('Azizbek')
my_list.show()
