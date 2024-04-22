# Pre-order traversal
def pre_order(node):
    result = []
    if not isinstance(node, Node):
        return []
    result += [node.data]
    if node.left:
        result += pre_order(node.left)
    if node.right:
        result += pre_order(node.right)

    return result

# In-order traversal
def in_order(node):
    result = []
    if not isinstance(node, Node):
        return []
    if node.left:
        result += in_order(node.left)
    result += [node.data]
    if node.right:
        result += in_order(node.right)

    return result

# Post-order traversal
def post_order(node):
    result = []
    if not isinstance(node, Node):
        return []
    if node.left:
        result += post_order(node.left)
    if node.right:
        result += post_order(node.right)
    result += [node.data]
    return result