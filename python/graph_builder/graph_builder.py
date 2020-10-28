from collections import defaultdict

# import by `from graph_builder.graph_builder import AdjacencyList`
# g = AdjacencyList()
# g.add_edge(5, 2)
# g.add_edge(5, 0)
# g.add_edge(4, 0)
# g.add_edge(4, 1)
# g.add_edge(2, 3)
# g.add_edge(3, 1)

class AdjacencyList:
    def __init__(self):
        # dictionary containing adjacency List
        self.__graph = defaultdict(list)
        self.__node_set = set([])
        self.__node_count = 0

    def add_edge(self, source_node, dest_node):
        self.__graph[source_node].append(dest_node)

        # keep track of unique node count
        for node in [source_node, dest_node]:
            if node not in self.__node_set:
                self.__node_count += 1
                self.__node_set.add(node)

    def __getitem__(self, key):
        return self.__graph[key]

    def node_count(self):
        return self.__node_count

    def keys(self):
        return self.__graph.keys()
