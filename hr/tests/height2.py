class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def getHeight(root):
    if root is None:
        return -1
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    return max(left_height, right_height) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(getHeight(root))
