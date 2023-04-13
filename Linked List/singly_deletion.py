class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def delete_at_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_at_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        
        prev.next = None

    def delete_at_position(self,position):
        temp = self.head.next
        prev = self.head
        for i in range(1,position-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None


    def display(self):
        temp = self.head

        if self.head is None:
            print('Empty linked list')
        
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=' ')
                temp = temp.next


L=SinglyLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
L.head.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
L.delete_at_begining()
L.delete_at_end()
L.delete_at_position(2)
L.display()
