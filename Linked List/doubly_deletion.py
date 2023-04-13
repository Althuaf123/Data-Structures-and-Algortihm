class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def delete_at_end(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next

        temp.prev = None
        before.next = None

    def delete_at_position(self,position):
        temp = self.head.next
        before = self.head
        for i in range(position-1):
            temp = temp.next
            before = before.next
        
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None 

    def display(self):
        if self.head is None:
            print('Empty linked list')

        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=' ')
                temp = temp.next



L = DoublyLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
n.next = n1
n1.prev = n
n2 = Node(30)
n1.next = n2
n2.prev = n1
n3 = Node(40)
n2.next = n3
n3.prev = n2
n4 = Node(50)
n3.next = n4
n4.prev = n3
L.delete_at_begining()
L.delete_at_end()
L.delete_at_position(1)
L.display()