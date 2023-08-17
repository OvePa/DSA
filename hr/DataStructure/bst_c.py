class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Method to insert a value into the binary search tree
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    # Recursive helper method to insert a value
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    # Method to perform an inorder traversal of the binary search tree
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    # Recursive helper method for inorder traversal
    def _inorder_recursive(self, current_node, result):
        if current_node is not None:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.value)
            self._inorder_recursive(current_node.right, result)


# Example usage
bst = BinarySearchTree()
values = [5, 3, 8, 2, 4, 7, 9]

# Insert values into the binary search tree
for value in values:
    bst.insert(value)

# Perform inorder traversal and print the sorted values
inorder_result = bst.inorder_traversal()
print(inorder_result)  # Output: [2, 3, 4, 5, 7, 8, 9]
