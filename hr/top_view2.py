class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def topView(root):
    if root is None:
        return

    # Define a class to store the node and its horizontal distance
    class QueueNode:
        def __init__(self, node, distance):
            self.node = node
            self.distance = distance

    # Initialize a dictionary to store the top view nodes
    top_view = {}

    # Initialize a queue for level order traversal
    queue = [QueueNode(root, 0)]

    while queue:
        current = queue.pop(0)
        if current.distance not in top_view:
            top_view[current.distance] = current.node.value

        if current.node.left:
            queue.append(QueueNode(current.node.left, current.distance - 1))
        if current.node.right:
            queue.append(QueueNode(current.node.right, current.distance + 1))

    # Print the top view nodes in order of horizontal distance
    for distance in sorted(top_view.keys()):
        print(top_view[distance], end=" ")


# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

topView(root)  # Output: 2 1 3 6
