def insert_target(arr, target):
    arr.append(target)
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_element
    
    return arr

input = [1,5,3,2,7,6,9,8]
print(insert_target(input,4))