class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class DeleteValue:
    def __init__(self):
        self.head = None

    def delete_specified_value(self,target):

        temp = self.head
        prev = None
       
        while temp:
            if temp.data == target:
                if prev:
                    prev.next = temp.next
                    temp.next = None
                else:
                    self.head = temp.next
                    temp.next = None
                    return
            else:
                prev = temp
                temp = temp.next



    def display(self):
        if self.head is None:
            print('Empty linked list')

        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=' ')
                temp = temp.next

L = DeleteValue()
n = Node(10)
L.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
L.delete_specified_value(10)
L.display()