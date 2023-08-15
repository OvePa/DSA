import math
import os
import random
import re
import sys


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def swapNodes(indexes, queries):
    def inorder(node, result):
        if node is None:
            return
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)

    def swap(node, depth, target_depth):
        if node is None:
            return
        swap(node.left, depth + 1, target_depth)
        swap(node.right, depth + 1, target_depth)
        if depth % target_depth == 0:
            node.left, node.right = node.right, node.left

    root = TreeNode(1)
    queue = [root]
    for left, right in indexes:
        current = queue.pop(0)
        if left != -1:
            current.left = TreeNode(left)
            queue.append(current.left)
        if right != -1:
            current.right = TreeNode(right)
            queue.append(current.right)

    results = []
    for query in queries:
        swap(root, 1, query)
        result = []
        inorder(root, result)
        results.append(result)

    return results


if __name__ == "__main__":
    fptr = open("pruebas.txt", "w")

    n = int(input("n > ").strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    print("Indexes: ", indexes)

    queries_count = int(input("q >").strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input("qi >").strip())
        queries.append(queries_item)

    print("Queries", queries)

    result = swapNodes(indexes, queries)

    fptr.write("\n".join([" ".join(map(str, x)) for x in result]))
    fptr.write("\n")

    fptr.close()
