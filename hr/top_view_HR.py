"""
Given a pointer to the root of a binary tree, print the top view of the binary tree.

The tree as seen from the top the nodes, is called the top view of the tree.

For example :

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top View : 1->2->5->6

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

1 2 5 6

Explanation

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
From the top, only nodes 1,2,5,6 are visible.
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


# Define a function to print the top view of a binary tree
def topView(root):
    if root is None:
        return  # If the tree is empty, exit the function

    # Define a class to represent nodes in the queue along with their distances
    # from the root
    class QueueNode:
        def __init__(self, node, distance):
            self.node = node
            self.distance = distance

    top_view = {}  # Dictionary to store the top view of the tree

    queue = [
        QueueNode(root, 0)
    ]  # Initialize the queue with the root node and its distance from the root

    # Perform a level order traversal to find the top view of the tree
    while queue:
        current = queue.pop(0)  # Get the front node from the queue

        # Check if the current distance is not already in the top view dictionary
        if current.distance not in top_view:
            # Add the current node's value to the top view dictionary
            top_view[current.distance] = current.node.info

        # Enqueue the left child if it exists along with its updated distance
        if current.node.left:
            queue.append(QueueNode(current.node.left, current.distance - 1))

        # Enqueue the right child if it exists along with its updated distance
        if current.node.right:
            queue.append(QueueNode(current.node.right, current.distance + 1))

    # Print the top view nodes in sorted order of distances
    for distance in sorted(top_view.keys()):
        print(top_view[distance], end=" ")


# This function prints the top view of a binary tree, which consists of the
# nodes visible when looking at the tree from the top.
# Nodes are printed in the order of their vertical distance from the root node.


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("Number of Nodes: "))

    arr = list(map(int, input("Array: ").split()))

    for i in range(t):
        tree.create(arr[i])

    topView(tree.root)
