# 2: Recursive Sort
from stack import MyStack
def sort_stack(stack):
    if (not stack.is_empty()):
        # Pop the top element off the stack
        value = stack.pop()
        # Sort the remaining stack recursively
        sort_stack(stack)
        # Push the top element back into the sorted stack
        insert(stack, value)

def insert(stack, value):
    if (stack.is_empty() or value < stack.peek()):
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)

if __name__ == "__main__" :
    # Creating and populating the stack
    stack_obj = MyStack()
    stack_obj.push(2)
    stack_obj.push(97)
    stack_obj.push(4)
    stack_obj.push(42)
    stack_obj.push(12)
    stack_obj.push(60)
    stack_obj.push(23)
    # Sorting the stack
    sort_stack(stack_obj)
    # Printing the sorted stack
    print("Stack after sorting")
    print([stack_obj.pop() for i in range(stack_obj.size())])
