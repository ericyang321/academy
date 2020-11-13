from union_find.index_union_find import IndexUnionFind


class Edge(object):
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost


def kruskals(edges, node_count):
    # finds and returns the shortest way to walk through
    # every node in the graph, no loops

    # in this implementation, node_count also doubles as unique
    # node ids from 0 - node_count
    if len(edges) == 0:
        return 0

    span_sum = 0
    sorted_edges = sorted(edges, lambda edge: edge.cost)
    uf = IndexUnionFind(node_count)

    for edge in sorted_edges:
        if uf.is_connected(edge.source, edge.destination):
            continue

        # union the edge if it's not a loop
        uf.union(edge.source, edge.destination)
        # add the cost of the edge
        span_sum += edge.cost

        # optimization: stop early if we've touched all nodes
        # assuming that node 0 is the root we start from
        if uf.component_size(0) == node_count:
            break

    # if not every node is accessible, a minimum spanning tree
    # is impossible
    if uf.component_size(0) != node_count:
        return None

    return span_sum
