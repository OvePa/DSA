"""
Write a function that takes a head node and an integer value n and then
returns the nth to last node in the linked list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nth_to_last_node1(n, head):
    left_pointer = head
    right_pointer = head

    for _ in range(n - 1):
        if not right_pointer.nextnode:
            raise LookupError("Error: n is larger than the linked list!")

        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)
    i = Node(9)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e
    e.nextnode = f
    f.nextnode = g
    g.nextnode = h
    h.nextnode = i

    target_node1 = nth_to_last_node1(3, a)  # 3
    print(target_node1.value)
