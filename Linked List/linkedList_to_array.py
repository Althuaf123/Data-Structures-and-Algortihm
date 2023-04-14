class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    
    def add_to_array(self):
        arr = []
        current_node = self.head
        while current_node is not None:
            arr.append(current_node.data)
            current_node = current_node.next
        return arr

   
L = SinglyLinkedList()
L.add_node(1)
L.add_node(2)
L.add_node(3)
L.add_node(4)
L.add_node(5)
arr = L.add_to_array()
print(arr)
