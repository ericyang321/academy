from heaps.min_priority_queue import MinPriorityQueue


def lazy_shortest_path(adjacency_list, start_node, end_node):
    """
    finds shortest exact path traversable from start node to all other nodes
    called lazy because the algorithm lazily deletes outdated (longer path) key
    value pairs

    to find MORE than just the distance and find the exact PATH, you need to keep track of
    the PREVIOUS node we took to get to a CURRENT node.

    maintain another `previous_node` hash data structure.
    {current_node: previous_node}, initially filled with 1.

    assuming a graph adjacency structure of:
    adjacency_list = {
        "U": {"V": 2, "W": 5, "X": 1},
        "V": {"U": 2, "X": 2, "W": 3},
        "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
        "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
        "Y": {"X": 1, "W": 1, "Z": 1},
        "Z": {"W": 5, "Y": 1},
    }
    """
    INF = float("inf")

    distances = {}
    previous_nodes = {}

    # initialize every node as "unreachable"
    for node in adjacency_list.keys():
        distances[node] = INF

    distances[start_node] = 0

    visited = set()
    pq = MinPriorityQueue([(0, start_node)])

    while len(pq) > 0:
        priority_queue_dist, node = pq.pop()
        visited.add(node)
        # optimization: skip over processing a node in the heap if we already found a less costly
        # traversal method out there.
        # this is to skip over "stale" node traversal paths in the heap that have high costs
        if distances[node] < priority_queue_dist:
            continue

        # iterate over every neighbor of a current node
        for neighbor, weight in adjacency_list[node].items():
            if neighbor in visited:
                continue

            # accumulated distance = shortest distance of CURRENT node + cost to traverse from current node to neighbor node
            # if new accumulated distance is shorter than what's already saved, update
            accumulated_distance = distances[node] + weight
            if accumulated_distance < distances[neighbor]:
                # save a parent relationship for the neighbor. but only save the node with smallest cost.
                previous_nodes[neighbor] = node
                distances[neighbor] = accumulated_distance

                # we only append to priority queue if the neighbor is a promising one that gave us a shorter distance.
                pq.append((accumulated_distance, neighbor))

    # reconstruct the shortest path with `previous_nodes`
    path = []
    if end_node not in distances or distances[end_node] == INF:
        return path

    at = end_node
    while at is not None and at in previous_nodes:
        path.append(at)
        at = previous_nodes.get(at, None)

    path.reverse()
    return path
