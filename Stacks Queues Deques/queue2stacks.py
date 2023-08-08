class Queue2Stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


if __name__ == "__main__":
    s = Queue2Stacks()

    for _ in range(10):
        s.enqueue(_)
        print("Item: ", _)

    for _ in range(10):
        print(s.dequeue())
