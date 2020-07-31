"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

has_common_ancestor(parent_child_pairs_1, 3, 8) => false
has_common_ancestor(parent_child_pairs_1, 5, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 9) => true
has_common_ancestor(parent_child_pairs_1, 1, 3) => false
has_common_ancestor(parent_child_pairs_1, 3, 1) => false
has_common_ancestor(parent_child_pairs_1, 7, 11) => true
has_common_ancestor(parent_child_pairs_1, 6, 5) => true
has_common_ancestor(parent_child_pairs_1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parent_child_pairs_2 = [
    (11, 10), (11, 12), (2, 3), (10, 2), (10, 5),
    (1, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

has_common_ancestor(parent_child_pairs_2, 4, 12) => true
has_common_ancestor(parent_child_pairs_2, 1, 6) => false
has_common_ancestor(parent_child_pairs_2, 1, 12) => false

n: number of pairs in the input
"""

from collections import deque

def build_ancestors(relationships, node):
    # find all accessible parents for node1 and save them into
    # a set. also use set as visited count
    q = deque([node])
    node_parents = set()
    while q:
        n = q.pop()
        # we don't want to add the node we're seeking parents of
        if n != node:
            node_parents.add(n)
        # skipping orphaned nodes
        if n not in relationships:
            continue

        for parent in relationships[n]:
            if parent not in node_parents:
                q.appendleft(parent)

    return node_parents

def has_common_ancestor(edges_array, node1, node2):
    if len(edges_array) == 0:
        return False

    # build O(1) access relationship hash of {child: [parent, parent...]}
    relationships = {}
    for parent, child in edges_array:
        if child not in relationships:
            relationships[child] = []

        relationships[child].append(parent)

    node1_parents = build_ancestors(relationships, node1)
    node2_parents = build_ancestors(relationships, node2)

    print(f"{node1}: {node1_parents}")
    print(f"{node2}: {node2_parents}")

    return len(node1_parents.intersection(node2_parents)) > 0

# # test example 1

# parent_child_pairs_1 = [
#     (1, 3),
#     (2, 3),
#     (3, 6),
#     (5, 6),
#     (5, 7),
#     (4, 5),
#     (4, 8),
#     (4, 9),
#     (9, 11),
#     (14, 4),
#     (13, 12),
#     (12, 9),
# ]

# assert has_common_ancestor(parent_child_pairs_1, 3, 8) is False
# assert has_common_ancestor(parent_child_pairs_1, 5, 8) is True
# assert has_common_ancestor(parent_child_pairs_1, 6, 8) is True
# assert has_common_ancestor(parent_child_pairs_1, 6, 9) is True
# assert has_common_ancestor(parent_child_pairs_1, 1, 3) is False
# assert has_common_ancestor(parent_child_pairs_1, 3, 1) is False
# assert has_common_ancestor(parent_child_pairs_1, 7, 11) is True
# assert has_common_ancestor(parent_child_pairs_1, 6, 5) is True
# assert has_common_ancestor(parent_child_pairs_1, 5, 6) is True

# # test example 2

# parent_child_pairs_2 = [
#     (11, 10),
#     (11, 12),
#     (2, 3),
#     (10, 2),
#     (10, 5),
#     (1, 3),
#     (3, 4),
#     (5, 6),
#     (5, 7),
#     (7, 8),
# ]

# assert has_common_ancestor(parent_child_pairs_2, 4, 12) is True
# assert has_common_ancestor(parent_child_pairs_2, 1, 6) is False
# assert has_common_ancestor(parent_child_pairs_2, 1, 12) is False
