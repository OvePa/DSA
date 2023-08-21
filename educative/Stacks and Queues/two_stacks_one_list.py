class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.top1 = -1
        self.top2 = self.size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value

        else:
            print("Stack Overflow")
            exit(1)

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print("Stack Overflow")
            exit(1)

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 -= 1
            return x
        else:
            print("Stack Underflow")
            exit(1)


if __name__ == "__main__":
    stack1 = TwoStacks(3)
    stack2 = TwoStacks(3)
    stack1.push1(1)
    stack1.push1(2)
    stack1.push1(3)
    for i in range(stack1.size):
        print(stack1.pop1())

    stack2.push2(4)
    stack2.push2(5)
    stack2.push2(6)
    for i in range(stack2.size):
        print(stack2.pop2())
