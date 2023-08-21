from stack import MyStack

# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


# We can use 2 stacks for this purpose,mainStack to store original values
# and tempStack which will help in enqueue operation.
# Main thing is to put first entered element at the top of mainStack


class newQueue:
    # Can use size from argument to create stack
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
            print(str(value) + "init main enqueued")
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # inserting the value in the queue
            self.main_stack.push(value)
            print(str(value) + "temp enqueued")
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    # Removes Element From Queue
    def dequeue(self):
        # If stack empty then return None
        if self.main_stack.is_empty():
            return None
        value = self.main_stack.pop()
        print(str(value) + " main dequeued")
        return value


if __name__ == "__main__":
    queue = newQueue()
    for i in range(5):
        queue.enqueue(i + 1)
    print("----------")
    for i in range(5):
        queue.dequeue()
