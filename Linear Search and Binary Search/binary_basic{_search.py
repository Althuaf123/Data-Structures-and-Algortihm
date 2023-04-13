L = []
n = int(input('Enter the number of elements: '))
print('Enter the elements: ')

for i in range(n):
    L.append(int(input()))
L.sort()
print('sorted list is: ',L)

target = int(input('enter the element to search for: '))
low = 0
high = len(L)-1
mid = 0

while low <= high:
    mid = (low+high)//2
    if L[mid] == target:
        print('Position of ',target,'is: ',mid+1)
        break    
    elif L[mid] > target:
        high = mid+1
    else:
        low = mid+1
else:
    print(target,' not found in the given list')