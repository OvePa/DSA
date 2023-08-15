class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.value, end=" ")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

postOrder(root)  # Output: 4 5 2 3 1
