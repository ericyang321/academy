from .min_priority_queue import MinPriorityQueue


def lazy_shortest_distance(adjacency_list, start_node):
    """
    finds shortest distances traversable from start node to all other nodes
    called lazy because the algorithm lazily deletes outdated (longer path) key
    value pairs

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
    distances = {}

    # initialize every node as "unreachable"
    for node in adjacency_list.keys():
        distances[node] = float("infinity")

    distances[start_node] = 0

    visited = set([])
    previous_nodes = {}
    pq = MinPriorityQueue([(0, start_node)])

    while len(pq) > 0:
        priority_queue_dist, node = pq.pop()
        visited.add(node)
        # optimization: skip over processing a node in the heap if we already found a less costly
        # traversal method out there.
        # this is to skip over "stale" nodes in the heap that have high costs
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
                pq.append((accumulated_distance, neighbor)

    # reconstruct the shortest path with `previous_nodes`


