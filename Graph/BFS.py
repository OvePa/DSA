graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"]),
}


def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


if __name__ == "__main__":
    print(bfs(graph, "A"))
