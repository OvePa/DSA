import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def levelOrderPrint(tree):
    if not tree:
        return

    nodes = collections.deque([tree])

    currentCount = 1
    nextCount = 0

    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1

        print(currentNode.val, end=", ")

        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1

        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1

        if currentCount == 0:
            print("\n")
            currentCount, nextCount = nextCount, currentCount


if __name__ == "__main__":
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)

    levelOrderPrint(r)
