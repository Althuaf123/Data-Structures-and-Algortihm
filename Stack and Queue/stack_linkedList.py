class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        value = int(input('Enter element to insert'))
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.top.next = None
        else:
            new_node.next = self.top
            self.top = new_node
        

    def pop(self):
        if self.top is None:
            print('Empty Stack')
        elif self.top.next is None:
            self.top = None
        else:
            temp = self.top
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print('Empty Stack')
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

S = Stack()
while(1):
    print('1-push, 2-pop, 3-display,any key to exit')
    option = int(input())
    if option == 1:
        S.push()
    elif option == 2:
        S.pop()
    elif option == 3:
        S.display()
    else:
        print('Exit')
        break
    