"""
Function Description

Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

getHeight or height has the following parameter(s):

root: a reference to the root of a binary tree.
Note -The Height of binary tree with single node is taken as zero.

Input Format

The first line contains an integer , the number of nodes in the tree.
Next line contains  space separated integer where th integer denotes node[i].data.

Note: Node values are inserted into a binary search tree before a reference to the tree's root node is passed to your function. In a binary search tree, all nodes on the left branch of a node are less than the node value. All values on the right branch are greater than the node value.

Output Format

Your function should return a single integer denoting the height of the binary tree.

Sample Input
7
3 5 2 1 4 6 7
Expected Output
3
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


# Define a function to calculate the height of a binary tree
def height(root):
    if root is None:
        return -1  # If the current node is None, return -1 to account for the
        # base case of an empty tree

    # Recursively calculate the height of the left subtree
    left_height = height(root.left)

    # Recursively calculate the height of the right subtree
    right_height = height(root.right)

    # Return the maximum height between the left and right subtrees,
    # plus 1 for the current node
    return max(left_height, right_height) + 1


# This function calculates the height of a binary tree, which is the maximum
# number of edges between the root and a leaf node.
# The height of an empty tree is -1, and the height of a tree with just the
# root is 0.


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("Number of Nodes> "))

    arr = list(map(int, input("Array> ").split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))
