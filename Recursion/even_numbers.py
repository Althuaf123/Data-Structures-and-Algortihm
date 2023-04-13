def even(n1,n2):
    if n2 < n1:
        return
    print(n1)
    return even(n1+2,n2)

n1 = int(input('Enter first number: '))
n2 = int(input('Enter last number: '))

if n1%2 == 0:
    n1=n1
else:
    n1=n1+1
even(n1,n2)