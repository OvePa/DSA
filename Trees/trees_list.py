def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == "__main__":
    r = BinaryTree(1)
    print(r)
    print(insertLeft(r, 2))
    print(insertLeft(r, 5))
    print(insertRight(r, 6))
    print(insertRight(r, 7))
    l = getLeftChild(r)
    print(l)
    setRootVal(l, 9)
    print(r)
