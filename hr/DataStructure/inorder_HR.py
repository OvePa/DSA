"""
Complete the inOrder function which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's inorder traversal as a single line of space-separated values.

Input Format

Our test code passes the root node of a binary tree to the inOrder function.

Output Format

Print the tree's preorder traversal as a single line of space-separated values.

Sample Input

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4
Sample Output

1 2 3 4 5 6
Explanation

The tree's inorder traversal results in  1 2 3 4 5 6 as the required result.
"""


# Define a class to represent individual nodes in a binary tree
class Node:
    def __init__(self, info):
        self.info = info  # Store the value of the node
        self.left = None  # Initialize left child as None
        self.right = None  # Initialize right child as None
        self.level = None  # Store the level of the node in the tree

    def __str__(self):
        return str(self.info)  # Return the string representation of the node's value


# Define a class to represent a binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize an empty binary search tree

    # Method to insert a new value into the binary search tree
    def create(self, val):
        if self.root == None:  # If the tree is empty, set the root as a
            self.root = Node(val)  # new node with the given value
        else:
            current = self.root  # Start at the root node

            while True:
                # This checks if the value to be inserted (val) is less
                # than the value of the current node (current.info).
                if val < current.info:
                    # This checks if the current node has a left child.
                    if current.left:
                        # If there is a left child, move the current pointer to
                        # the left child node. This allows the loop to continue
                        # down the left subtree.
                        current = current.left
                    else:
                        current.left = Node(val)  # If there's no left child,
                        break  # create a new node with the
                        # value and set it as the left child
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)  # If there's no right child,
                        break  # create a new node with the
                        # value and set it as the right child
                else:
                    break  # If the value is equal to the current node's value,
                    # do nothing (assuming duplicates are not allowed)


# Define a function to perform an in-order traversal of a binary tree
def inOrder(root):
    if root is None:
        return  # If the current node is None, return and exit the function

    inOrder(root.left)  # Recursively traverse the left subtree

    # Print the value of the current node followed by a space,
    # using 'end=" "' to print on the same line
    print(root.info, end=" ")

    inOrder(root.right)  # Recursively traverse the right subtree


# This function performs an in-order traversal, visiting nodes in the order of
# left subtree, current node, and then right subtree.
# It prints the values of the nodes in ascending order for a binary search tree.


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("Number of Nodes: "))

    arr = list(map(int, input("Array: ").split()))

    for i in range(t):
        tree.create(arr[i])

    inOrder(tree.root)
