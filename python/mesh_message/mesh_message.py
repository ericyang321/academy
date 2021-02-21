from collections import deque


def trace(ancestor_trail, src, dest):
    path = []
    node = dest

    while node != src:
        path.append(node)
        node = ancestor_trail[node]

    path.append(src)

    return list(reversed(path))


def shortest_path(adjacency_list, src, dest):
    if src == dest:
        return [src]

    ancestor_trail = {}

    q = deque([src])

    while len(q) > 0:
        node = q.popleft()

        # no neighbors
        if node not in adjacency_list:
            continue

        # already processed the node
        if node in ancestor_trail:
            continue

        for neighbor in adjacency_list[node]:
            if neighbor not in ancestor_trail:
                ancestor_trail[neighbor] = node

            if neighbor == dest:
                return trace(ancestor_trail, src, dest)

            q.append(neighbor)

    raise ValueError("Cannot reach destination")


if __name__ == "__main__":
    network = {
        "Min": ["William", "Jayden", "Omar"],
        "William": ["Min", "Noam"],
        "Jayden": ["Min", "Amelia", "Ren", "Noam"],
        "Ren": ["Jayden", "Omar"],
        "Amelia": ["Jayden", "Adam", "Miguel"],
        "Adam": ["Amelia", "Miguel", "Sofia", "Lucas"],
        "Miguel": ["Amelia", "Adam", "Liam", "Nathan"],
        "Noam": ["Nathan", "Jayden", "William"],
        "Omar": ["Ren", "Min", "Scott"],
    }

    print(shortest_path(network, "Jayden", "Noam"))
