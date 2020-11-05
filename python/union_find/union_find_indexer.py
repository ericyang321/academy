class UnionFindIndexer(object):
    # this implementation of Union Find uses array idx as unique ids for nodes
    # to use this class you need to map an array index to a node element
    # as the unions and finds in this class return array indices and not the
    # elements themselves.
    def __init__(self, size):
        if size <= 0:
            raise ValueError

        # contains data about how many nodes are in each component
        self.components_sizes = []
        self.parents = []
        # tracks total count of components in the union find
        self.total_components = size

        for idx in range(size):
            # all nodes are initialized as root node
            self.parents.append(idx)
            # every node is a component size of 1 of itself
            self.components_sizes.append(1)

    def find(self, idx):
        # find which component / root node (AKA component ID) a node belongs to
        root_idx = idx
        # find root node
        while root_idx != self.parents[root_idx]:
            root_idx = self.parents[root_idx]

        # path compression: compress the path you just traversed all the way
        # from idx -> root_idx to save time
        # compression gives this data structure Amortized run time.
        while root_idx != idx:
            # for every node, save a reference to their original parents,
            # reset the parent reference to root_idx, and then traverse to the
            # parent node and update _its_ parent to root_idx, continuously repeating
            parent_idx = self.parents[idx]
            self.parents[idx] = root_idx
            idx = parent_idx

        return root_idx

    def recursive_find(self, idx):
        if idx == self.parents[idx]:
            return idx

        # assign the parent of every traversed idx along the way to the rootidx
        # after callback from base case
        self.parents[idx] = self.recursive_find(self.parents[idx])
        return self.parents[idx]

    def union(self, idx, other_idx):
        # already unified under the same set
        if self.is_connected(idx, other_idx):
            return False

        root = self.find(idx)
        other_root = self.find(other_idx)

        # merge the two roots together. merge the smaller one into the larger one.
        if self.components_sizes[root] > self.components_sizes[other_root]:
            self.components_sizes[root] += self.components_sizes[other_root]
            self.parents[other_root] = root
        else:
            self.components_sizes[other_root] += self.components_sizes[root]
            self.parents[root] = other_root

        self.total_components -= 1

    def is_connected(self, idx, other_idx):
        return self.find(idx) == self.find(other_idx)

    def component_size(self, idx):
        return self.component_sizes[idx]
