def move(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    return arr

input = [1,0,1,0,2,5,2,7,0,0,3,0,6,0,3,0,0,0]
print(move(input))