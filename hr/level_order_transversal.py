import collections


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


def levelOrder(root):
    # Write your code here
    if not root:
        return

    nodes = collections.deque([root])

    currentCount = 1
    nextCount = 0

    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1

        print(currentNode.info, end=" ")

        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1

        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1

        if currentCount == 0:
            # print("\n")
            currentCount, nextCount = nextCount, currentCount


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input("> "))

    arr = list(map(int, input("> ").split()))

    for i in range(t):
        tree.create(arr[i])

    levelOrder(tree.root)
