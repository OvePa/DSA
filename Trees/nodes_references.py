from tree_traversal import preorder, postorder, inorder


class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


if __name__ == "__main__":
    r = BinaryTree("a")
    print(r.getRootVal())
    r.insertLeft("b")
    print(r.getLeftChild().getRootVal())
    r.insertRight("c")
    print(r.getRightChild().getRootVal())
    r.insertLeft("d")
    r.insertRight("e")
    print(r.getLeftChild().getRootVal())
    print(r.getRightChild().getRootVal())
    print("Preorder")
    preorder(r)
    print("Inorder")
    inorder(r)
    print("Postorder")
    postorder(r)
