class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def node_at_begining(self,data):
        new_node = Node(data)
        temp = self.head
        temp.prev = new_node
        new_node.next = temp
        self.head = new_node

    def node_at_end(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        

    def node_at_position(self,position,data):
        new_node = Node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        new_node.data = data
        new_node.prev = temp
        new_node.next = temp.next
        temp.next = new_node
        temp.next.prev = new_node

    def display(self):
        if self.head is None:
            print('Empty doubly linked list')

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
L.node_at_begining(5)
L.node_at_end(45)
L.node_at_position(2,25)
L.display()