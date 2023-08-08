# FIFO


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


if __name__ == "__main__":
    s = Queues()
    print("Is empty:", str(s.isEmpty()))
    for _ in range(10):
        s.enqueue(_ * 3)
        print("Enqueue!")

    print("Is empty:", str(s.isEmpty()))
    for _ in range(5):
        print("Dequeue:", s.dequeue())

    print("Is empty:", str(s.isEmpty()))
