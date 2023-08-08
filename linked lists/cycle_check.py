"""
Given a singly linked list, write a function which takes in the first node
in a singly linked list and returns a boolean indicating if the linked list
contains a "cycle".
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def cycle_check(node):
    f_node = node

    while node.nextnode != None:
        node = node.nextnode
        if node.nextnode == f_node:
            return True

    return False


def cycle_check1(node):
    marker1 = None
    marker2 = None

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = a

    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.nextnode = y
    y.nextnode = z

    print(cycle_check(a))
    print(cycle_check(x))
