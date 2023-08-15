"""
Complete the preOrder function which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

Input Format

Our test code passes the root node of a binary tree to the preOrder function.

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

1 2 5 3 4 6
Explanation

The preorder traversal of the binary tree is printed.
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Define a function to perform a pre-order traversal of a binary tree
def preOrder(root):
    if root is None:
        return  # If the current node is None, return and exit the function

    # Print the value of the current node followed by a space, using 'end=" "'
    # to print on the same line
    print(root.info, end=" ")

    preOrder(root.left)  # Recursively traverse the left subtree
    preOrder(root.right)  # Recursively traverse the right subtree


# This function performs a pre-order traversal, visiting nodes in the order of
# the current node, left subtree, and then right subtree.
# It prints the values of the nodes in a sequence that is useful for creating
# a copy of the tree.


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("Number of Nodes: "))

    arr = list(map(int, input("Array: ").split()))

    for i in range(t):
        tree.create(arr[i])

    preOrder(tree.root)
