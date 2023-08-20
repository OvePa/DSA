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

        print("Length: ", counter)
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

    def detect_loop(self):
        if self.is_empty():
            return False

        one_step = self.get_head()
        two_step = self.get_head()

        while one_step and two_step and two_step.next_node:
            one_step = one_step.next_node
            two_step = two_step.next_node.next_node
            if one_step == two_step:
                return True

        return False

    def find_mid(self):
        length = self.length()
        counter = 0
        if length % 2 == 1:
            counter = length // 2
        else:
            counter = (length / 2) - 1

        currentNode = self.get_head()
        while currentNode:
            if counter == 0:
                print(currentNode.val)
                return currentNode.val
            counter -= 1
            currentNode = currentNode.next_node

    def remove_duplicates(self):
        if self.is_empty():
            return None

        if self.get_head().next_node is None:
            return self

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node
            while inner_node:
                if inner_node.next_node:
                    if outer_node.val == inner_node.next_node.val:
                        new_next_node = inner_node.next_node.next_node
                        inner_node.next_node = new_next_node
                    else:
                        inner_node = inner_node.next_node
                else:
                    inner_node = inner_node.next_node
            outer_node = outer_node.next_node
        return self

    def union(self, list2):
        if self.is_empty():
            return list2
        elif list2.is_empty():
            return self

        l1 = self.get_head()
        l2 = list2.get_head()

        while l1.next_node:
            l1 = l1.next_node

        l1.next_node = l2

        print("Union:")
        l1 = self.remove_duplicates()
        return l1

    def intersection(self, list2):
        result = LinkedList()
        visited_nodes = set()
        current_node = self.get_head()

        while current_node:
            value = current_node.val
            if value not in visited_nodes:
                visited_nodes.add(value)
            current_node = current_node.next_node

        start = list2.get_head()

        while start:
            value = start.val
            if value in visited_nodes:
                result.insert_at_head(start.val)

            start = start.next_node
        result.remove_duplicates()
        result.print_list()
        return result

    def find_nth(self, n):
        # Write your code here
        length = self.length()
        if n > length:
            return -1
        else:
            counter = length - n

        currentNode = self.get_head()

        while counter != 0:
            currentNode = currentNode.next_node
            counter -= 1

        print("Value: ", currentNode.val)
        return currentNode.val

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

    print("*" * 7)
    print("Reversed Linked List")
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in lists!")
    for i in range(7):
        lst.insert_at_head(i)
    lst.print_list()
    lst.reverse()
    lst.print_list()

    print("*" * 7)

    print("Floyd's cycle-finding algorithm")
    lst = LinkedList()

    lst.insert_at_head(21)
    lst.insert_at_head(14)
    lst.insert_at_head(7)

    # Adding a loop
    head = lst.get_head()
    node = lst.get_head()

    for i in range(4):
        if node.next_node is None:
            node.next_node = head.next_node
            break
        node = node.next_node

    print(lst.detect_loop())

    print("*" * 7)
    print("Finding Mid!")
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in lists!")
    for i in range(7):
        lst.insert_at_tail(i + 1)

    lst.print_list()
    lst.find_mid()
    print("*" * 7)

    print("Removing Duplicates!")
    lst = LinkedList()
    lst.insert_at_head(7)
    lst.insert_at_head(7)
    lst.insert_at_head(7)
    lst.insert_at_head(22)
    lst.insert_at_head(14)
    lst.insert_at_head(21)
    lst.insert_at_head(14)
    lst.insert_at_head(7)

    lst.print_list()
    lst.remove_duplicates()
    lst.print_list()

    print("*" * 7)
    print("Union!")
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in list1!")
    for i in range(5):
        lst.insert_at_head(i)
    lst.print_list()
    print("*" * 7)

    lst2 = LinkedList()
    lst2.print_list()
    print("Inserting values in list2!")
    for i in range(5):
        lst2.insert_at_tail(i + 3)
    lst2.print_list()

    lst.union(lst2)
    lst.print_list()
    print("*" * 7)
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in list 1!")
    for i in range(5):
        lst.insert_at_head(i)

    lst2 = LinkedList()
    lst2.print_list()
    print("Inserting values in list2!")
    for i in range(5):
        lst2.insert_at_tail(i + 3)
    print("Intersection!")
    print("Lista 1")
    lst.print_list()
    print("Lista 2")
    lst2.print_list()
    lst.intersection(lst2)
    print("*" * 7)
    """

    print("Find Nth!")
    lst = LinkedList()
    lst.print_list()
    print("Inserting values in list!")
    for i in range(10):
        lst.insert_at_head(i + 1)

    lst.print_list()
    lst.find_nth(3)
    print("*" * 7)


