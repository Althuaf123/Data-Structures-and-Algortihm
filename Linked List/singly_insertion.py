class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertion_at_begining(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            node_at_begining = Node(data)
            node_at_begining.next = self.head
            self.head = node_at_begining
        
    def insertion_at_end(self,data):
        node_at_end = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node_at_end

    def insertion_at_position(self,position,data):
        node_at_position = Node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        
        node_at_position.next = temp.next
        temp.next = node_at_position

    def display(self):
        temp = self.head

        if self.head is None:
            print('Empty Linked List')
        
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=' ')
                temp = temp.next


L = SinglyLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
L.head.next = n1
n2 = Node(30)
n1.next = n2
L.insertion_at_begining(5)
L.insertion_at_end(40)
L.insertion_at_position(1,23)
L.display()
