def all_paths(arr):
    if not arr:
        return []

    def dfs(index, path, result):
        if index >= len(arr) or arr[index] is None:
            return

        path.append(arr[index])

        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child >= len(arr) or arr[left_child] is None:
            if right_child >= len(arr) or arr[right_child] is None:
                result.append(path[:])
        else:
            dfs(left_child, path, result)

        if right_child < len(arr) and arr[right_child] is not None:
            dfs(right_child, path, result)

        path.pop()

    result = []
    dfs(0, [], result)
    return result

arr = [1, 2, 3, 4, None, 5]
paths = all_paths(arr)
print("All possible paths:")
for path in paths:
    print(path)
