def inorder_traversal(arr, index):
    if index < len(arr) and arr[index] is not None:
        inorder_traversal(arr, 2 * index + 1)
        print(arr[index], end=" ")
        inorder_traversal(arr, 2 * index + 2)

def preorder_traversal(arr, index):
    if index < len(arr) and arr[index] is not None:
        print(arr[index], end=" ")
        preorder_traversal(arr, 2 * index + 1)
        preorder_traversal(arr, 2 * index + 2)

def postorder_traversal(arr, index):
    if index < len(arr) and arr[index] is not None:
        postorder_traversal(arr, 2 * index + 1)
        postorder_traversal(arr, 2 * index + 2)
        print(arr[index], end=" ")

arr = [4, 2, 6, 1, 3, 5, 7]
print("Inorder Traversal:")
inorder_traversal(arr, 0)
print("\nPreorder Traversal:")
preorder_traversal(arr, 0)
print("\nPostorder Traversal:")
postorder_traversal(arr, 0)
