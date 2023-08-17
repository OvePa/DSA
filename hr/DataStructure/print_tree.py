def printLevels(root):
    if root is None:
        return

    queue = [(root, 0)]
    current_level = 0
    nodes = []

    while queue:
        node, level = queue.pop(0)

        if level != current_level:
            print(f"Level {current_level}: {nodes}")
            current_level = level
            nodes = []

        nodes.append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    print(f"Level {current_level}: {nodes}")
