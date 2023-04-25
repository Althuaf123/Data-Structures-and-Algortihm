def ascending(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr [i], arr[j] = arr[j],arr[i]
            else:
                continue
    return arr

arr = [5,4,8,3,9,2,1,3]
print(ascending(arr))