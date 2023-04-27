def mergesort(arr1,arr2):
    result = []
    i = 0
    j = len(arr2) -1
    while (i < len (arr1) or j >= 0):
        if (j < 0 or (i < len(arr1) and arr1[i] < arr2[j])):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j -= 1
    
    return result

arr1 = [1,3,4,6,8]
arr2 = [9,7,5,2]
print(mergesort(arr1,arr2))