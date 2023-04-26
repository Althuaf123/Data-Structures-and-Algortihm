def first_pivot(arr,first,last):
    pivot = arr[first]
    left = first+1
    right = last
    while True:


        while left <= right and arr[left] >= pivot:
            left += 1
        while left <= right and arr[right] <= pivot:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[first],arr[right] =  arr[right],arr[first]
    return right

def quicksort(arr,first,last):
    if first<last:
        p = first_pivot(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)

arr= [2,4,5,1,8,9,3,4]
length = len(arr)
quicksort(arr,0,length-1)
print(arr)