class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,'-->',end = ' ')
            temp = temp.next


def array_to_linkedList(arr):
    L = SinglyLinkedList()
    for i in range(len(arr)):
        L.addNode(arr[i])
    return L

arr = [1,2,3,4,5,6]
L = array_to_linkedList(arr)
L.display()
