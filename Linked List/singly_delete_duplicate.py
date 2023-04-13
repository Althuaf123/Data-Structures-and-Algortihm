class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def delete_diplicate(self):
        if self.head is None:
            return
        
        current_node = self.head
        while current_node is not None:

            prev_node = current_node
            next_node = current_node.next
            while next_node is not None:
                if next_node.data == current_node.data:
                    prev_node.next = next_node.next
                else:
                    prev_node = next_node
                next_node = next_node.next
            current_node = current_node.next

  
    def display(self):
    
        if self.head is None:
            print('Empty linked list')
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end = ' ')
                temp = temp.next

L = SinglyLinkedList()
n = Node(11)
L.head = n
n1 = Node(12)
n.next = n1
n2 = Node(11)
n1.next = n2
n3 = Node(12)
n2.next = n3
n4 = Node(14)
n3.next = n4
L.display()
L.delete_diplicate()
L.display()