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
    indexes = [[2, 3], [-1, -1], [-1, -1]]  # 2
    queries = [1, 1]
    # swapNodes(indexes, queries)
    indexes2 = [[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]  # 2  # 3  # 3
    queries2 = [2]
    # swapNodes(indexes2, queries2)
    indexes3 = [
        [2, 3],  # i + 2
        [4, -1],  # i + 3
        [5, -1],  # i + 3
        [6, -1],  # i + 4
        [7, 8],  # i + 4
        [-1, 9],  # i + 5
        [-1, -1],  #
        [10, 11],  # i + 5
        [-1, -1],
        [-1, -1],
        [-1, -1],
    ]
    queries3 = [2, 4]
    print(swapNodes(indexes, queries))
    print(swapNodes(indexes2, queries2))
    print(swapNodes(indexes3, queries3))
