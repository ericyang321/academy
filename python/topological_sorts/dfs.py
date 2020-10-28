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
