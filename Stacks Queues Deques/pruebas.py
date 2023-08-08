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


class Queues(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print("Is empty:", str(s.isEmpty()))
    for _ in range(10):
        s.push(_ * 3)

    print("Is empty:", str(s.isEmpty()))

    print("Peek: ", str(s.peek()))
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Peek: ", str(s.peek()))
    print("Size:", str(s.size()))
    print("Is empty:", str(s.isEmpty()))

    print("Queues")
    s = Queues()
    print("Is empty:", str(s.isEmpty()))
    for _ in range(10):
        s.enqueue(_ * 3)
        print("Enqueue!")

    print("Is empty:", str(s.isEmpty()))
    for _ in range(5):
        print("Dequeue:", s.dequeue())

    print("Is empty:", str(s.isEmpty()))

    print("Deque")

    d = Deque()
    print("Is empty:", str(d.isEmpty()))
    for _ in range(10):
        d.addFront(_ * 3)
        print("Add Front!")

    for _ in range(10):
        d.addRear(_ * 3)
        print("Add Rear!")

    print("Is empty:", str(d.isEmpty()))
    for _ in range(5):
        print("Remove Front:", d.removeFront())

    for _ in range(5):
        print("Remove Rear:", d.removeFront())

    print("Is empty:", str(d.isEmpty()))
