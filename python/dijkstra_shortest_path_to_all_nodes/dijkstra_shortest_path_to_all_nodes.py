import heapq


class MinPriorityQueue(object):
    def __init__(self, heap):
        self.heap = heap

    def append(self, elem):
        heapq.heappush(self.heap, elem)
        return elem

    def pop(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


def shortest_distances(g, start_n):
    """
    also checks for the exact shortest path taken
    """
    paths = {}
    visited = set([])
    for node in g.keys():
        paths[node] = (float("infinity"), [])

    paths[start_n] = (0, [start_n])

    pq = MinPriorityQueue([(0, start_n)])

    while len(pq) > 0:
        distance_so_far, node = pq.pop()

        if node in visited:
            continue

        visited.add(node)

        for neighbor_node, weight in g[node].items():
            accumulated_distance = distance_so_far + weight

            if accumulated_distance < paths[neighbor_node][0]:
                new_data = (accumulated_distance, paths[node][1] + [neighbor_node])
                paths[neighbor_node] = new_data

                pq.append((accumulated_distance, neighbor_node))

    return paths


# graph = {
#     "U": {"V": 2, "W": 5, "X": 1},
#     "V": {"U": 2, "X": 2, "W": 3},
#     "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
#     "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
#     "Y": {"X": 1, "W": 1, "Z": 1},
#     "Z": {"W": 5, "Y": 1},
# }

# shortest_distances(graph, "X")
