"""
we define a binary tree to be a binary search tree with the following ordering requirements:

The data value of every node in a node's left subtree is less than the data value of that node.
The data value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

It must return a boolean denoting whether or not the binary tree is a binary search tree
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Define a function to check if a binary tree is a valid binary search tree (BST)
def isBST(root, min_value=float("-inf"), max_value=float("inf")):
    if root is None:
        return True  # An empty tree is considered a valid BST

    # Check if the value of the current node is within the allowed range
    if root.val <= min_value or root.val >= max_value:
        return False  # If not, the tree is not a valid BST

    # Recursively check the left subtree, updating the maximum value constraint
    # The left subtree values must be less than the value of the current node
    # The maximum value constraint is updated to the value of the current node
    left_valid = isBST(root.left, min_value, root.val)

    # Recursively check the right subtree, updating the minimum value constraint
    # The right subtree values must be greater than the value of the current node
    # The minimum value constraint is updated to the value of the current node
    right_valid = isBST(root.right, root.val, max_value)

    # Both subtrees must be valid BSTs for the entire tree to be a valid BST
    return left_valid and right_valid


# This function checks whether a given binary tree is a valid binary search tree (BST),
# ensuring that each node's value is greater than its left subtree values and smaller than its right subtree values.

# Note: The 'root' argument should be a TreeNode object with 'left', 'right', and 'value' properties.


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("Number of Nodes: "))

    arr = list(map(int, input("Array: ").split()))

    for i in range(t):
        tree.create(arr[i])

    print(arr)

    root = Node(4)
    root.left = Node(6)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print(isBST(root))  # Output: False
    print(isBST(tree.root))  # Output: True
