class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preOrder(root):
    if root is None:
        return
    print(root.value, end=" ")
    preOrder(root.left)
    preOrder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preOrder(root)
