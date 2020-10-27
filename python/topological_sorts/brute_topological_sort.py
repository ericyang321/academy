# from graph_builder.graph_builder import AdjacencyList
from collections import deque


def dfs(adjacency_list, node, visited, stack):
    visited.add(node)

    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            dfs(adjacency_list, neighbor, visited, stack)

    stack.appendleft(node)


def topological_sort(adjacency_list):
    visited = set([])
    stack = deque([])

    for node in list(adjacency_list.keys()):
        if node not in visited:
            dfs(adjacency_list, node, visited, stack)

    return list(stack)


# if __name__ == "__main__":
#     g = AdjacencyList()
#     g.add_edge(5, 2)
#     g.add_edge(5, 0)
#     g.add_edge(4, 0)
#     g.add_edge(4, 1)
#     g.add_edge(2, 3)
#     g.add_edge(3, 1)

#     print(topological_sort(g))
