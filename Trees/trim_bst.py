# Define a function to trim a binary search tree within a given range
def trimbst(tree, minVal, maxVal):
    if not tree:
        return None  # If the tree is empty, return None

    # Recursively trim the left and right subtrees
    tree.left = trimbst(tree.left, minVal, maxVal)
    tree.right = trimbst(tree.right, minVal, maxVal)

    # Check if the current node's value is within the specified range
    if minVal <= tree.val <= maxVal:
        return tree  # If yes, return the current node

    # If the current node's value is less than the minimum value, discard the left subtree
    if tree.val < minVal:
        return tree.right

    # If the current node's value is greater than the maximum value, discard the right subtree
    if tree.val > maxVal:
        return tree.left


# This function trims a binary search tree by removing nodes whose values fall outside the specified range [minVal, maxVal].
# It returns the root of the trimmed tree.

# Note: The 'tree' argument should be a TreeNode object with 'left', 'right', and 'val' properties.
