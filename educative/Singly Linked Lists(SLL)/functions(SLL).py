from linkedList import Node, LinkedList

# Access HeadNode => list.getHead()
# Check if list is empty => list.isEmpty()
# Node class  { int data ; Node nextElement;}

# Inserts a value at the end of the list


def insert_at_tail(lst, value):
    # Creating a new node
    new_node = Node(value)

    # Check if the list is empty, if it is simply point head to new node
    if lst.get_head() is None:
        lst.head_node = new_node
        return

    # if list not empty, traverse the list to the last node
    temp = lst.get_head()

    while temp.next_node:
        temp = temp.next_node

    # Set the nextElement of the previous node to new node
    temp.next_node = new_node
    return


def search(lst, value):
    # Start from first element
    current_node = lst.get_head()

    # Traverse the list till you reach end
    while current_node:
        if current_node.val == value:
            return True  # value found
        current_node = current_node.next_node

    return False  # value not found


# Recursive
def search_recursive(node, value):
    # Base case
    if not node:
        return False  # value not found

    # check if the node's data matches our value
    if node.val is value:
        return True  # value found

    # Recursive call to next node in the list
    return search(node.next_element, value)


def delete_at_head(lst):
    # Get Head and firstElement of List
    first_element = lst.get_head()

    # if List is not empty then link head to the
    # nextElement of firstElement.
    if first_element is not None:
        lst.head_node = first_element.next_node
        first_element.next_element = None
    return


def delete(lst, value):
    deleted = False
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is Empty")
        return deleted
    current_node = lst.get_head()  # Get current node
    previous_node = None  # Get previous node
    if current_node.val == value:
        lst.delete_at_head()  # Use the previous function
        deleted = True
        return deleted

    # Traversing/Searching for Node to Delete
    while current_node is not None:
        # Node to delete is found
        if value == current_node.val:
            # previous node now points to next node
            previous_node.next_element = current_node.next_node
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_node

    if deleted == False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted


if __name__ == "__main__":
    # Print
    lst = LinkedList()
    lst.print_list()
    insert_at_tail(lst, 0)
    lst.print_list()
    insert_at_tail(lst, 1)
    lst.print_list()
    insert_at_tail(lst, 2)
    lst.print_list()
    insert_at_tail(lst, 3)
    lst.print_list()
    # Search
    lst = LinkedList()
    lst.insert_at_head(4)
    lst.insert_at_head(10)
    lst.insert_at_head(40)
    lst.insert_at_head(5)
    lst.print_list()
    print(search(lst, 4))
    # Deletion
    lst = LinkedList()
    for i in range(11):
        lst.insert_at_head(i)

    lst.print_list()

    delete_at_head(lst)
    delete_at_head(lst)

    lst.print_list()
    # Delete
    lst = LinkedList()
    lst.insert_at_head(1)
    lst.insert_at_head(4)
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.print_list()
    delete(lst, 4)
    lst.print_list()
