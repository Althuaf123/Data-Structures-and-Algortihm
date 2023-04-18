def enqueue():
    n = int(input("Enter the value: "))
    queue.append(n)
    print()

def dequeue():
    if len(queue) == 0:
        print('Empty queue')
    
    else:
        print(queue[0], 'is deleted from queue')
        del queue[0]
    print()

def display():
    if len(queue) == 0:
        print('queue is empty')
    else:
        print('elements of queue are: ')
        for elements in queue:
            print(elements)
    print()
queue = list()

while(1):
    option = int(input('1 for enqueue, 2 for dequeue, 3 for display, any key for exit: '))
    if option == 1:
        enqueue()
    elif option == 2:
        dequeue()
    elif option == 3:
        display()
    else:
        print('Exit')
        break