def descending_order(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                arr[i], arr[j] = arr[j],arr[i]
            else:
                continue
    return arr

arr = [2,3,9,1,8,5,6,7,2,4]
print(descending_order(arr))