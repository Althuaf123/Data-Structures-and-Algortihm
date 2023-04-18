def push():
    n  = int(input('Enter the element to be inserted into stack'))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,'is inserted into stack')
    print()

def pop():
    if len(stack) == 0:
        print('Stack is empty')
    else:
        print(stack[0],'is deleted from stack')
        del stack[0]
    print
    ()

def display():
    if len(stack) == 0:
        print('stack is empty')
    else:
        print('elements of stack are: ')
        for elements in stack:
            print(elements)
        print('Top of the stack is: ',stack[0])
    print()

stack = list()
while(1):
    print("1 for Push,  2 for pop, 3 for display, any key to exit")
    option = input()
    if option == '1':
        push()
    elif option == '2':
        pop()
    elif option == '3':
        display()
    else:
        print('Exit')
        break