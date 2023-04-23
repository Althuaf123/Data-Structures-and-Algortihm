def ascending(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                pass
    return arr

input = [10,15,15,23,0,4]
print(ascending(input))