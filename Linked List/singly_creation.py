class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        temp = self.head
        ele=[]
        if self.head is None:
            print("Empty Linked list")
        else:
            temp = self.head
            while temp:
                print(temp.data, '-->' ,end=' ')
                ele.append(temp.data)
                temp = temp.next

        print(ele)


L = SinglyLinkedList()
n1 = Node(10)
L.head = n1
n2 = Node(20)
L.head.next = n2
n3 = Node(30)
n2.next = n3
L.display()