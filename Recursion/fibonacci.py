# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)   

# n = int(input('Enter a number: '))
# for i in range(n+1):
#     print(fibonacci(i),end = ' ')

def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    else:
        print(a)
        return fibonacci(n-1, b, a+b)
print(fibonacci(10))

# to print the n-th element of a fibonacci series

def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fibonacci(n-1, b, a+b)
print(fibonacci(10))