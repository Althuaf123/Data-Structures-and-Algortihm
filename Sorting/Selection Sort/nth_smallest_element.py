def nth_element(arr,n):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr [i], arr[j] = arr[j],arr[i]
            else:
                continue
    return arr[n-1],arr

n = int(input('Enter the position: '))
print()
arr = [3,6,1,7,2,9,7,2,4,5,1]
print(nth_element(arr,n))