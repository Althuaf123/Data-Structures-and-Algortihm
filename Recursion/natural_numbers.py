# def natural_numbers(n):
#     if n:
#         return n
#     else:
#         return natural_numbers(n-(n-1))

# n = int(input('Enter a number: '))
# for i in range(1,n+1):
#     print(natural_numbers(i),end=' ')

# def natural_numbers(n):
#     if n>0:
#         natural_numbers(n-1)
#         print(n,end = ' ')

# natural_numbers(10)

def get_natural_numbers(n):
    if n == 1:
        return [1]
    else:
        natural_numbers = get_natural_numbers(n-1)
        natural_numbers.append(n)
        return natural_numbers
print(get_natural_numbers(5))