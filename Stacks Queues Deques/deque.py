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
