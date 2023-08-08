"""
Write a function to reverse a Linked List in place. The function will take in
the head of the list as input and return the new head of the list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.nextnode  # b

        current.nextnode = previous  # a

        previous = current  # a
        current = nextnode  # b

    return previous.value


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d

    print("a.nextnode.value:", a.nextnode.value)  # 2
    print("b.nextnode.value:", b.nextnode.value)  # 3
    print("c.nextnode.value:", c.nextnode.value)  # 4

    print(reverse(a))

    print("d.nextnode.value:", d.nextnode.value)  # 3
    print("c.nextnode.value:", c.nextnode.value)  # 2
    print("b.nextnode.value:", b.nextnode.value)  # 1
