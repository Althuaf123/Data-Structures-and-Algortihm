def swap_count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    return count

input = [2,1,6,4,8,4,7,3,1]
print(swap_count(input))