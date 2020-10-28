from collections import defaultdict, deque


def kahns_algorithm(adjacency_list):
    in_degree = defaultdict(int)

    # write all in_degree for all nodes, to and from
    # O(n + e)
    for source_node in adjacency_list.keys():
        if source_node not in in_degree:
            in_degree[source_node] = 0

        for dest_node in adjacency_list[source_node]:
            in_degree[dest_node] += 1

    q = deque([])

    # enqueue all nodes with in_degree of 0 to start
    for node in in_degree.keys():
        if in_degree[node] == 0:
            q.appendleft(node)

    visited_nodes = 0
    stack = []

    while q:
        node = q.pop()
        stack.append(node)

        for neighbor in adjacency_list[node]:
            in_degree[neighbor] -= 1
            # if in-degree becomes zero (meaning that node has been walked to completely), enqueue it
            if in_degree[neighbor] == 0:
                q.appendleft(neighbor)

        visited_nodes += 1

    if visited_nodes != adjacency_list.node_count():
        print("There's a cycle in graph")

    return stack
