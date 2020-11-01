from dijkstras_algorithm.lazy_shortest_distance import lazy_shortest_distance
from dijkstras_algorithm.lazy_shortest_path import lazy_shortest_path


adjacency_list = {
    "U": {"V": 2, "W": 5, "X": 1},
    "V": {"U": 2, "X": 2, "W": 3},
    "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
    "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
    "Y": {"X": 1, "W": 1, "Z": 1},
    "Z": {"W": 5, "Y": 1},
}

print(
    lazy_shortest_path(adjacency_list, "U", "W")
)
