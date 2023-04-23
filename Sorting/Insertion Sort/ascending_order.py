def ascending_order(arr):
    for i in range(1,len(arr)):
        current_element = arr[i]
        index = i
        while current_element < arr[index-1] and index > 0:
            arr[index] = arr[index-1]
            index = index-1
        arr[index] = current_element
    return arr

input = [2,5,3,8,2,1,9,1,0]
print(ascending_order(input))