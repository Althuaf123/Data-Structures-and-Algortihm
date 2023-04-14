def binary_search(arr,low,high,target):
    if high >= low:
        mid = (high+low)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binary_search(arr,low,mid-1,target)
        
        else:
            return binary_search(arr,mid+1,high,target)
        
    else:
        return -1

arr = [1,2,3,4,5,6]
low = 0
target = 4
result = binary_search(arr,low,(len(arr)-1),target)
print(result)