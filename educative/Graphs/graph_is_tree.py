"""
Problem statement#
Here’s the basic difference between a graph and a tree. A graph can only be a
tree under two conditions:

* There are no cycles.
* The graph is connected.

A graph is connected when there is a path between every pair of vertices. In a
connected graph, there are no unreachable vertices. Each vertex must be
connected to every other vertex through either a direct edge or a graph traversal.
"""

from graph import Graph

# We only need Graph for this Question!


def is_tree(g):
    # All vertices unvisited
    visited = [False] * g.vertices

    # Check cycle using recursion stack
    # Also mark nodes visited to check connectivity
    if check_cycle(g, 0, visited, -1):
        return False

    # Check if all nodes we visited from the source (graph is connected)
    for i in range(len(visited)):
        # Graph is not connected
        if not visited[i]:
            return False
    # Not cycle and connected graph
    return True


def check_cycle(g, node, visited, parent):
    # Mark node as visited
    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node
    while adjacent:
        if not visited[adjacent.data]:
            if check_cycle(g, adjacent.data, visited, node):
                return True

        # If adjacent is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            # Cycle found
            return True
        adjacent = adjacent.next_element

    return False


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print(is_tree(g))
