# not completed yet

class TravellingSalesman(object):
    def __init__(self, matrix, start_node=0):
        # requires an adjacency matrix, and a unique start node id (integer)

        # state flags and instance variables
        self.matrix = matrix
        self.nodes_count = len(self.matrix)
        self.solved = False
        self.start_node = start_node

        # return results
        self.tour = []
        self.min_tour_cost = float("inf")

        self._validate_inputs()

    def get_tour(self):
        if not self.solved:
            self._solve()

        return self.tour

    def get_tour_cost(self):
        if not self.solved:
            self._solve()

        return self.min_tour_cost

    def _solve(self):
        if self.solved:
            return

        # the set up: this is your dynamic programming smallest work
        # find the optimal distance from start node to 1 other node (length = 2)
        # since it's just two nodes, you just save the cost from start node -> node as is.
        memo = [
            [None for _ in range(1 << self.nodes_count)]
            for _ in range(self.nodes_count)
        ]

        for destination_node in range(self.nodes_count):
            # we don't count the start node
            if destination_node == self.start_node:
                continue

            # 1 << start node will give you the bit position of start_node
            # 1 << destination node will give you the bit position of the destination node
            # | them together, and you get a bin number with both those nodes flipped, indicating the state of both those nodes VISITED
            # example:
            #   1 << 0 = 0b000 (1)
            #   1 << 2 = 0b100 (4)
            #   1 << 0 | 1 << 2 = 0b1100 (5)
            memo[destination_node][
                1 << self.start_node | 1 << destination_node
            ] = self.matrix[self.start_node][destination_node]

        # we just did start_node -> node. now we continue with path lengths greater than 2
        for r in range(3, self.nodes_count):
            combinations = self.create_combinations(r, self.nodes_count):
                # we skip over any subpaths without start node in it

    def create_combinations(self, one_bits_count, total_bits):
        pass

    def not_in(self):
        pass

    def _finished_traversing(self, visited_state):
        # The finished state is when the finished state mask has all bits are set to
        # one (meaning all the nodes have been visited).
        return visited_state == ((1 << self.nodes_count) - 1)

    def _validate_inputs(self):
        if self.nodes_count <= 2:
            raise ValueError(
                "Travelling salesman calculation requires at least 3 nodes."
            )

        if self.nodes_count != len(self.matrix[0]):
            raise ValueError("Matrix must be a square, like an adjacency matrix.")

        if (
            self.start_node is None
            or self.start_node < 0
            or self.start_node >= self.nodes_count
        ):
            raise ValueError(
                f"Start node value is not correct. Must be between 0 and {self.nodes_count}. Instead found {self.start_node}"
            )

        if self.nodes_count > 32:
            raise ValueError(
                "Matrix is too large. More than 32 nodes requires more resources than most commodity hardward an handle."
            )


# testing
matrix = [[10000 for _ in range(6)] for _ in range(6)]
matrix[1][4] = matrix[4][1] = 2
matrix[4][2] = matrix[2][4] = 4
matrix[2][3] = matrix[3][2] = 6
matrix[3][0] = matrix[0][3] = 8
matrix[0][5] = matrix[5][0] = 10
matrix[5][1] = matrix[1][5] = 12
print(matrix)

solver = TravellingSalesman(matrix)

tour = solver.get_tour()
cost = solver.get_tour_cost()
