#using head recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter a number: "))
output = factorial(n)
print(output)

#using tail recursion
def factorial(n, result=1):
    if n == 0:
        return result
    else:
        return factorial(n-1, n*result)
print(factorial(n))

