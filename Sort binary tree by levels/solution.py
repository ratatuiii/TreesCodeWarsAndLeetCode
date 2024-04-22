from collections import deque

def tree_by_levels(node):
    if not node:
        return []

    result = []
    queue = deque([node])

    while queue:
        node_temp = queue.popleft()
        result.append(node_temp.value)
        if node_temp.left:
            queue.append(node_temp.left)
        if node_temp.right:
            queue.append(node_temp.right)

    return result