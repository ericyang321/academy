from .min_priority_queue import MinPriorityQueue

def eager_shortest_distance(adjacency_list, start_node):
    """
    requires an Indexed Priority Queue

    finds shortest distances traversable from start node to all other nodes
    unlike the lazy version, eager version actively deletes stale nodes with costly paths.

    you want to use an eager version in dense (many connections) graphs.
    lazy implementation ends up enqueueing a lot of stale distance-node pairs.

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
