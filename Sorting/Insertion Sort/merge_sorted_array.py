def merge(arr1, arr2):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr1.insert(i, arr2[j])
            j += 1
    if j < len(arr2):
        arr1.extend(arr2[j:])
    return arr1

input1 = [1,3,4,7]
input2 = [2,5,6,8,9]
print(merge(input1,input2))