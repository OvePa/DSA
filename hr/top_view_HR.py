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


def topView(root):
    if root is None:
        return

    # Define a class to store the node and its horizontal distance
    class QueueNode:
        def __init__(self, node, distance):
            self.node = node
            self.distance = distance

    # Initialize a dictionary to store the top view nodes
    top_view = {}

    # Initialize a queue for level order traversal
    queue = [QueueNode(root, 0)]

    while queue:
        current = queue.pop(0)
        if current.distance not in top_view:
            top_view[current.distance] = current.node.info

        if current.node.left:
            queue.append(QueueNode(current.node.left, current.distance - 1))
        if current.node.right:
            queue.append(QueueNode(current.node.right, current.distance + 1))

    # Print the top view nodes in order of horizontal distance
    for distance in sorted(top_view.keys()):
        print(top_view[distance], end=" ")


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("Number of Nodes: "))

    arr = list(map(int, input("Array: ").split()))

    for i in range(t):
        tree.create(arr[i])

    topView(tree.root)
