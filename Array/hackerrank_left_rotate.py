def rotate(d,arr):
    new =arr[:]
    for i in range (len(arr)):
        arr[i-d] = new[i]
    return arr

print(rotate(2,[1,2,3,4,5]))