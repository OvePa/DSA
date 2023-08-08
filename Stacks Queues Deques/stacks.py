# LIFO


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    for _ in range(10):
        s.push(_ * 3)

    print("Is empty:", str(s.isEmpty()))

    print("Peek: ", str(s.peek()))
    print("Pop:", s.pop())
    print("Peek: ", str(s.peek()))
    print("Size:", str(s.size()))
