class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def reverse_list(self):
        prev_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node


    def display(self):
        temp = self.head
        print (temp.next)
        while temp:
            print(temp.data, '-->', end = ' ')
            temp = temp.next

L = SinglyLinkedList()
n = Node(10)
L.head = n
n1 = Node(15)
n.next = n1
n2 = Node(20)
n1.next = n2
n3 = Node(25)
n2.next = n3
L.reverse_list()
L.display()
