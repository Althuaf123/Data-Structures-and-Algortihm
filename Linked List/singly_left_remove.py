#remove the value at the previous node of a linked list if the value of the current node is given:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class RemoveLeft:
    def __init__(self):
        self.head = None
    
    def remove_left(self,value):
        prev = self.head
        current  = self.head.next
        if prev == value:
            return
        elif prev.next.data == value:
            prev.next = None
            self.head = current
        else:
            while current.next is not None:
                if current.next.data == value:
                    prev.next = current.next
                    current = None
                    return
                prev = prev.next
                current = current.next
        
    def display(self):
        temp = self.head

        if self.head is None:
            print('Empty linked list')
        else:
            while temp:
                print(temp.data,'-->',end=" ")
                temp = temp.next

L = RemoveLeft()
n = Node(2)
L.head = n
n1 = Node(4)
n.next = n1
n2 = Node(10)
n1.next = n2
n3 = Node(25)
n2.next = n3
L.remove_left(2)
L.display()