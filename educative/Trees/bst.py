from node import Node


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    print(BST.root.val)
