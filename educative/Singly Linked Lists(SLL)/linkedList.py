import time


class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_node = self.head_node
        self.head_node = temp_node
        return self.head_node

    def insert_at_tail(self, data):
        if self.head_node is None:
            self.head_node = Node(data)
        else:
            currentNode = self.head_node
            while currentNode.next_node is not None:
                currentNode = currentNode.next_node

            currentNode.next_node = Node(data)

            return currentNode

    def search(self, k):
        if self.head_node is None:
            return

        currentNode = self.get_head()
        while currentNode.next_node is not None:
            if currentNode.val == k:
                print("Found!")
                return True
            else:
                currentNode = currentNode.next_node
        print("Not Found!")
        return False

    def delete_at_head(self):
        first_element = self.get_head()
        if first_element is not None:
            self.head_node = first_element.next_node
            first_element.next_node = None
            print("Deleted!")
            return

    def delete(self, k):
        if self.is_empty():
            print("List is Empty!")
            return

        currentNode = self.head_node
        previousNode = None
        if currentNode.val == k:
            self.delete_at_head()
            return True

        while currentNode.next_node is not None:
            if currentNode.val == k:
                previousNode.next_node = currentNode.next_node
                currentNode.next_node = None
                print("Deleted!")
                return True
            previousNode = currentNode
            currentNode = currentNode.next_node
        print("Not Found!")
        return False

    def length(self):
        if self.is_empty():
            print("List Empty!")
            return 0
        counter = 0
        currentNode = self.head_node

        while currentNode:
            counter += 1
            currentNode = currentNode.next_node

        print(counter)
        return counter

    def reverse(self):
        if self.is_empty():
            return
        currentNode = self.get_head()
        prevNode = None
        nextNode = None

        while currentNode:
            nextNode = currentNode.next_node
            currentNode.next_node = prevNode
            prevNode = currentNode
            currentNode = nextNode

            self.head_node = prevNode
        return self.head_node

    # Print
    def print_list(self):
        if self.is_empty():
            print("List Empty!")
            return False
        temp = self.head_node
        while temp.next_node is not None:
            print(temp.val, end=" -> ")
            temp = temp.next_node
            time.sleep(1)
        print(temp.val, "-> None")
        return True


if __name__ == "__main__":
    """
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in lists!")
    for i in range(5):
        lst.insert_at_head(i)
    lst.print_list()
    print("*" * 7)

    lst2 = LinkedList()
    lst2.print_list()
    print("Inserting values in lists!")
    for i in range(5):
        lst2.insert_at_tail(i)
    lst2.print_list()
    print("*" * 7)

    print("Searching")
    lst.search(3)
    lst2.search(7)
    print("*" * 7)

    print("Deletion at head")
    lst.print_list()
    lst.delete_at_head()
    lst.print_list()
    print("*" * 7)


    print("Deletion by Value")
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in lists!")
    for i in range(5):
        lst.insert_at_head(i)
    lst.print_list()
    print("First element: 4")
    lst.delete(4)
    lst.print_list()
    print("Element 2")
    lst.delete(2)
    lst.print_list()
    print("Element 7")
    lst.delete(7)
    lst.print_list()
    print("*" * 7)

    print("Length")
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in lists!")
    for i in range(7):
        lst.insert_at_head(i)
    lst.print_list()
    print("Length: ", lst.length())
    """
    print("Reversed Linked List")
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in lists!")
    for i in range(7):
        lst.insert_at_head(i)
    lst.print_list()
    lst.reverse()
    lst.print_list()
