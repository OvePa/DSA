from print_tree import printLevels

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
def isBST(root):
    stack = []  # Stack to help traverse the tree
    prev_value = 0  # Initialize the previous value with 0

    current = root  # Start from the root node
    while current or stack:
        while current:
            stack.append(current)  # Push the current node onto the stack
            current = current.left  # Move to the left child

        current = stack.pop()  # Pop a node from the stack

        # Check if the current node's value is less than the previous value
        if current.val < prev_value:
            return False  # If not, the tree is not a valid BST

        prev_value = current.val  # Update the previous value
        current = current.right  # Move to the right child

    return True  # If traversal completes without issues, the tree is a valid BST


# This function checks whether a given binary tree is a valid
# binary search tree (BST).
# It uses an iterative approach with a stack to perform an in-order
# traversal while maintaining the BST property.


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
    printLevels(root)
