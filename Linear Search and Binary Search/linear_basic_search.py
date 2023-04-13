L = []
n = int(input('Enter the number of elements in the list: '))
print('Enter',n,' elements: ')
for i in range(n):
    L.append(int(input()))

target = int(input('Enter the number to be found: '))
for i in range(len(L)-1):
    if L[i] == target:
        print('Position of the number is : ',i+1)
        break

else:
    print('Number not found in the given list')


#we can use membership operator instead of using 'for loop'

# if target in l:
#     print('The position of the element is: ',L.index(target)+1)

