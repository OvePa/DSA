import collections

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


# Import the 'collections' module to use the 'deque' data structure
import collections


# Define a function to perform level order traversal of a binary tree
def levelOrder(root):
    if not root:
        return  # If the tree is empty, exit the function

    # Create a deque (double-ended queue) to hold nodes for traversal
    nodes = collections.deque([root])
    currentCount = 1  # Counter for the current level's nodes
    nextCount = 0  # Counter for the next level's nodes

    # Perform the level order traversal using a while loop
    while len(nodes) != 0:
        currentNode = nodes.popleft()  # Get the node at the front of the deque
        currentCount -= 1  # Decrease the count of remaining nodes at the current level
        print(currentNode.info, end=" ")  # Print the value of the current node

        # Enqueue the left child of the current node if it exists
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1

        # Enqueue the right child of the current node if it exists
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1

        # Check if all nodes at the current level have been processed
        if currentCount == 0:
            currentCount, nextCount = nextCount, currentCount
            # Swap the counters to move to the next level


# This function performs a level order traversal of a binary tree,
# visiting nodes level by level from left to right.
# It prints the values of the nodes in the order they are encountered.


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("Number of Nodes: "))

    arr = list(map(int, input("Array: ").split()))

    for i in range(t):
        tree.create(arr[i])

    preOrder(tree.root)
