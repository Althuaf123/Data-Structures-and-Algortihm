def is_valid_bst(arr):
    def inorder_traversal(index):
        nonlocal prev
        if index >= len(arr) or arr[index] is None:
            return True

        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if not inorder_traversal(left_child):
            return False

        if prev is not None and prev >= arr[index]:
            return False

        prev = arr[index]

        return inorder_traversal(right_child)

    prev = None
    return inorder_traversal(0)


arr = [4, 2, 6, 1, 3, 5, 7] 
is_valid = is_valid_bst(arr)
print(is_valid)