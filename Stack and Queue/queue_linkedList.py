class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self):
        data = int(input("enter value: "))
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print()
    
    def dequeue(self):
        if self.rear is None or self.front is None:
            print('Empty Queue')
        elif self.front == self.rear:
            print(self.front.data, 'is deleted')
            self.front = None
        else:
            print(self.front.data, 'is deleted')
            temp = self.front
            self.front = temp.next
            temp = None
        print()

    def display(self):
        if self.front is None:
            print('Empty Queue')

        else:
            print('Elements of queue are: ')
            temp = self.front
            while temp:
                print(temp.data, end=' ')
                temp = temp.next
        print()

q = Queue()
while(1):
    print('1 for Enqueue, 2 for Dequeue, 3 for Display, any other key to exit')
    option = int(input('Enter an option: '))
    if option == 1:
        q.enqueue()
    elif option == 2:
        q.dequeue()
    elif option == 3:
        q.display()
    else:
        print('Exit')
        break
             